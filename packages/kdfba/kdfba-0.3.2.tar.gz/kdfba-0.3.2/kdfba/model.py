

### cobra.Model的子类model
## 读取字符串形式的酶动力学模型并修改对应reaction上下限的方法
## 修改优化目标的方法
###

from cobra import Model, Reaction
from typing import TYPE_CHECKING, Dict, Iterable, List, Optional, Tuple, Union
from dfba.reactions import dReaction
from warnings import warn
import re

class dModel(Model):
    def __init__(self, id_or_model: Union[str, "Model", None] = None, name: Optional[str] = None):
        super().__init__(id_or_model, name)
        self.sub_objectives =  None
        self.sub_objective_directions = None
        self.fraction_of_optimum = None
        self.dReactions = list()
        self.volume = 1e-15  # 字符串类型，计算时转化为float  表示单个细胞体积，默认为大肠杆菌体积，单位L
        self.weight = 3e-13  # 字符串类型，计算时转化为float  表示单个细胞干重，默认为大肠杆菌干重，单位g
        self.dilrate = 0  # 稀释率


    def __is_right_direction(self, sub_objective_direction):
        if (sub_objective_direction is "maximum") or (sub_objective_direction is "minimum"):
            return True
        else:
            return False

    def __is_right_objective(self, sub_objective):
        if sub_objective in self.reactions:
            return True
        else:
            return False

    # FVA目标设置
    def change_objective(
            self,
            main_objective: str,  ## 主要优化目标
            main_objective_direction: str,  ## 主要优化目标优化方向
            sub_objectives: List = None,  ## 次级优化目标（Reaction类型列表，包含多个反应  # 12.18补充，元素既可为反应也可为字符串）
            sub_objective_directions: List = None,  ## 次级优化目标方向（列表，一一对应多个反应）
            fraction_of_optimum = 1  ## 需达成主要优化目标值的比例，可在该比例下扩展一定优化空间
    ):
        # 在cobra中有错误处理机制
        self.objective = main_objective
        self.objective_direction = main_objective_direction

        # 在次级优化目标首个位置加入主要目标，方便fva直接计算
        sub_objectives.insert(0, main_objective)
        sub_objective_directions.insert(0, main_objective_direction)

        # 将sub_objectives里的字符串转化为对应的reaction类型
        objectives = [self.reactions.get_by_id(sub_objective) if not isinstance(sub_objective, dReaction) else sub_objective for sub_objective in sub_objectives]

        # 判断输入的次级优化目标在不在model反应列表中
        bool_list = list(map(self.__is_right_objective, objectives))
        if all(bool_list):
            self.sub_objectives = objectives
        else:
            bool_list = [not i for i in bool_list]
            invalid_list = [m and n for m, n in zip(bool_list, objectives)]
            index = [invalid_list.index(x) for x in invalid_list if x != 0]
            raise ValueError(f"不合规定次级优化目标 '{invalid_list[index[0]]}'.")

        # 再判断输入的次级优化目标方向是不是'maximum'或'minimum'
        if all(list(map(self.__is_right_direction, sub_objective_directions))):
            self.sub_objective_directions = sub_objective_directions
        else:
            raise ValueError(f"不合规定的次级优化方向输入, 请输入'maximum'或'minimum'.")

        # 判断输入的优化比例在不在0~1之间
        if fraction_of_optimum>=0 and fraction_of_optimum<=1:
            self.fraction_of_optimum = fraction_of_optimum
        else:
            raise ValueError(f"不合规定的优化比例值 '{fraction_of_optimum}'.")




    # 根据酶动力学模型修改对应方程
    def modify_reaction(
            self,
            reaction_id: str,  ## 需要修改的反应id
            bound_direction: str,  ## 修改反应的上限还是下限？（输入应为: 'upper', 'lower', 'both'）
            equation: str,  ## 修改后的反应方程
            is_volume=True  ## 判断输入的酶动力学模型是以体积为单位还是以干重为单位
    ):

        # 处理已经在dReaction列表中已有的反应，如果要修改只能删了重建
        for drxn in self.dReactions:
            if drxn.reaction.id == reaction_id:
                drxn.reaction_id = reaction_id
                drxn.bound_direction = bound_direction
                drxn.equation = equation
                return

        # 判断输入的bound_direction是否符合要求
        if (not bound_direction.startswith("upper")) and (not bound_direction.startswith("lower")) and (not bound_direction.startswith("both")):
            raise ValueError(f"'{bound_direction}'并非可设置的反应上下限, 请输入'upper', 'lower'或'both'.")

        dreaction = dReaction(self.reactions.get_by_id(reaction_id), bound_direction, equation, is_volume)

        self.dReactions.append(dreaction)


    # 用于删除已修改的反应
    def del_reaction(
        self,
        reaction_id: str
    ):
        for i in range(0, len(self.dReactions)):
            dReaction = self.dReactions[i]
            if dReaction.reaction.id == reaction_id:
                del self.dReactions[i]
                print(f"已删除反应'{reaction_id}'")
                break
            if i == (len(self.dReactions)-1):
                warn("未曾修改该反应, 本次删除失败")


    #  更改模型对应细胞的体积和干重, 在flux值和反应速率换算时有用, 具体为 反应速率 = flux * (Weigth/Volume)
    def modify_attribute(
        self,
        volume: str,
        weight: str
    ):
        volume = str(volume)
        weight = str(weight)

        #  引入正则表达式, 判断输入是否为科学计数法
        pat = re.compile('^-?([1-9]{1}|[1-9]?\.[0-9]+)[eE][+\-]?0?[1-9]+0*$')
        pat_float = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')  #  科学计数法接近于1或大于1时自动转化为float类型, 所以还需要判断是否为float类型

        matchObj1_volume = re.search(pat, volume)
        matchObj2_volume = re.match(pat_float, volume)
        if matchObj1_volume or matchObj2_volume:
            self.volume = volume
        else:
            raise ValueError(f"'{volume}'并非符合规范的科学计数法, 请参照'1e-15'形式输入.")

        matchObj1_weight = re.search(pat, weight)
        matchObj2_weight = re.match(pat_float, weight)
        if matchObj1_weight or matchObj2_weight:
            self.weight = weight
        else:
            raise ValueError(f"'{weight}'并非符合规范的科学计数法, 请参照'1e-15'形式输入.")
            

    #  更改dilution rate
    def modify_dilution_rate(
        self,
        rate: float
    ):
        if (rate<0) or (rate>1):
            raise ValueError(f"'{rate}'并非符合规范的速率, 请在0到1的范围内输入")
        self.dilrate = rate
