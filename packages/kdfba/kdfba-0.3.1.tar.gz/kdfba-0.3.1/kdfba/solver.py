
from cobra.flux_analysis import flux_variability_analysis
from cobra.exceptions import OptimizationError
from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Tuple, Union
from scipy.integrate import solve_ivp
from tqdm import tqdm
import numpy as np
import pandas as pd
import re


def simulate(
        models_dict: dict,  # model列表
        states: dict,  # 各种物质的初始状态，键是物质名(菌浓度用x_(model名)表示), 值是浓度(或flux)值
        derivatives_description: dict,  # 导数关系
        times: float,  # 模拟时长, 单位h
        steps=1000,  # 模拟步数, 步数越多越精确
        loopless=False  ##  loopless参数，在FVA计算时使用loopless算法会更精确但运算量更大
):

    infeasible_event.epsilon = 1e-16
    infeasible_event.direction = -1
    infeasible_event.terminal = True
    calculate_derivatives.pbar = None

    #  按传入的state键作为变量名，储存对应初始浓度数据
    states_var = globals()
    model_names = list(models_dict.keys())
    states_names = list(states.keys())
    for state_name in states_names:
        if state_name in model_names:  # 处理输入的菌落初始浓度的变量命名与model变量命名相同的情况  浓度统一用x_(model名)表示
            states_var['x_%s' % state_name] = states[state_name]
        else:
            states_var['%s' % state_name] = states[state_name]

    #  调用ode求解微分方程
    with tqdm() as pbar:
        calculate_derivatives.pbar = pbar

        params = (models_dict, states, derivatives_description, loopless)
        sim_times = np.linspace(0, times, steps)
        states_values = list(states.values())
        sim_results = solve_ivp(fun=calculate_derivatives,
                                t_span=(sim_times.min(),
                                        sim_times.max()),
                                y0=states_values,
                                t_eval=sim_times,
                                rtol=1.e-6,
                                atol=1.e-6,
                                # events=infeasible_event,
                                method='BDF',
                                args=(params,))

    return sim_results


def calculate_derivatives(t, states_value, params):

    #  按调用函数传入的state键作为变量名，储存这个函数传入的浓度数据
    models_dict, states, derivatives_description, loopless = params[0], params[1], params[2], params[3]

    var = globals()
    states_names = list(states.keys())
    for i in range(0, len(states_value)):
        if (states_value[i] < 0):
            states_value[i] = 0

        var['%s' % states_names[i]] = states_value[i]

    model_names = list(models_dict.keys())
    for model_name in model_names:
        #  读取每个模型中修改后的酶动力学反应
        model_temp = models_dict[model_name]
        dreactions = model_temp.dReactions

        #  根据酶动力学模型计算flux值
        for dreaction in dreactions:
            var['flux'] = 0
            if dreaction.is_volume:  # 以体积为单位，则计算flux时需要转化单位
                exec(
                    "var['flux'] = (" + dreaction.equation + ') * (model_temp.volume / model_temp.weight)')  ## ？？测试一下state里没有eqution对应物质的情况
            else:
                exec("var['flux'] = " + dreaction.equation)

            if dreaction.bound_direction.startswith("upper"):
                if dreaction.reaction.lower_bound > var['flux']:
                    var['flux'] = dreaction.reaction.lower_bound
                dreaction.reaction.upper_bound = var['flux']

            elif (dreaction.bound_direction.startswith("lower")):
                if dreaction.reaction.upper_bound < var['flux']:
                    var['flux'] = dreaction.reaction.upper_bound
                dreaction.reaction.lower_bound = var['flux']

            elif (dreaction.bound_direction.startswith("both")):
                dreaction.reaction.upper_bound = 1000
                dreaction.reaction.lower_bound = -1000  ## 避免上下限调整时出bug
                dreaction.reaction.upper_bound = var['flux']
                dreaction.reaction.lower_bound = var['flux']

        sub_objectives = model_temp.sub_objectives
        if sub_objectives is not None:
            sub_objectives_str = [sub_objective.id for sub_objective in sub_objectives]
            sub_objective_directions = model_temp.sub_objective_directions
            try:
                flux_values = flux_variability_analysis(model_temp, reaction_list=sub_objectives,
                                                        fraction_of_optimum=model_temp.fraction_of_optimum,
                                                        loopless=loopless)

            except OptimizationError:
                rows = len(sub_objectives)
                data = [[0] * 2] * rows
                flux_values = pd.DataFrame(data, columns=['minimum', 'maximum'], index=sub_objectives_str,
                                           dtype=float)

            # 用于判断是否需要结束求解的变量
            global objective_value
            objective_value = flux_values.at[sub_objectives[0].id, sub_objective_directions[0]]

            #  得到次级目的反应的flux值，变量名为model名+_+reaction_id
            # rxnsFluxValue = globals()
            for i in range(0, len(sub_objectives)):
                ##  这里就表示如果要算某些反应的flux值(比如时间导数那里有这个反应的话)，就必须加入到sub_objectives中. 不过也可以优化，只不过到时候要在solution里面去找对应的
                var[model_name + '_M_' + sub_objectives[i].id] = flux_values.at[
                    sub_objectives[i].id, sub_objective_directions[i]]

        ##  根据输入的时间导数公式和优化后得到的flux，计算时间导数并得到外界物质浓度变化情况
        derivatives = []
        derivative = globals()
        rxnsFluxValue_keys = list(var.keys())
        derivatives_keys = list(derivatives_description.keys())
        for state_name in states_names:
            derivative['d'] = 0
            if state_name.startswith("x_"):  # 计算菌落生长率对应时间导数
                # derivative = 0
                model_name = state_name.split("_", 1)[1]  # 得到state中的model名
                model_mu = model_name + '_M_' + derivatives_description[model_name]  # 优化后的生长率flux值变量名
                if model_mu in rxnsFluxValue_keys:  # 计算了这个菌的生长率, derivatives就不为0
                    dilution_rate = models_dict[model_name].dilrate
                    derivative['d'] = var[state_name] * var[model_mu] - var[state_name] * dilution_rate
                else:
                    solution = models_dict[model_name].optimize()
                    derivative['d'] = solution.fluxes['%s' % derivatives_description[model_name]]
            elif derivatives_description[state_name] == '0' or derivatives_description[state_name] == 0:
                pass
            elif state_name in derivatives_keys:  # 要求计算这种物质时间导数
                derivative_description = derivatives_description[state_name]  # 得到该物质的计算公式
                items = re.split('[+-]', derivative_description)

                reactions = globals()
                for item in items:
                    if item != '':
                        item = item.strip()
                        model_name = (item.split("_", 1)[0])
                        flux_name = (item.split("_", 1)[1])

                        model_weight = 'x_' + model_name
                        item_temp = model_name + '_M_' + flux_name

                        if item_temp in reactions.keys():
                            exec('var[item] =' + model_weight + '*' + item_temp)
                        else:

                            solution = models_dict[model_name].optimize()
                            if solution.status == "infeasible":
                                solution.fluxes = solution.fluxes * 0
                            flux = solution.fluxes['%s' % flux_name]

                            exec('var[item] =' + model_weight + '* flux')

                exec("derivative['d']=" + derivative_description)

            derivatives.append(derivative['d'])

        if calculate_derivatives.pbar is not None:
            calculate_derivatives.pbar.update(1)
            calculate_derivatives.pbar.set_description('t = {:.3f}'.format(t))

    return np.array(derivatives)


def infeasible_event(t, y, args):
    global objective_value
    return objective_value - infeasible_event.epsilon
