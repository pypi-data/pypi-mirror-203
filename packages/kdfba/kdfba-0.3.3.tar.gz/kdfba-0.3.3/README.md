# dFBApy - 动态通量平衡分析&&酶动力学模型 in Python

## 介绍

--------

#### 什么是dFBApy
dFBApy基于python包**CORBApy**[[1]](#1)进行开发，在其基础上引入**酶动力学模型**，并新增dFBA方法用于预测时间尺度上的微生物生长代谢状况，最终得到一套基于COBRA模型的动态通量平衡分析工具包。

#### dFBApy可实现
对改造后的工程菌生长代谢情况进行定量的模拟，以预测实验设计的可行性，并从预测结果中得到实验改进方向的指导。

## 安装dFBApy

----------

使用pip从PyPI上安装dFBApy，建议在虚拟环境中进行此操作
```
pip install kinetics-dfba
```

## 使用说明

----------

#### 1. 读取sbml, json, mat以及yaml文件

```
from dio import dio
io = dio()
Ec1 = io.read_sbml_dModel('../iAF1260.xml')
```
调用dio类，使用dio对象的函数读取保存在文件的model信息，返回dModel类型数据

**· read_sbml_dModel(filename)->dModel**

**· load_json_dModel(filename)->dModel**

**· load_matlab_dModel(filename, variable_name, inf)->dModel**

**· load_yaml_dModel(filename)->dModel**

#### 2. 修改dModel相关信息

dModel数据包含了基因组规模代谢模型(Genome-scale Metabolic models， GEMs)，其表示一种微生物中存在的所有生化反应，而这些反应的集合形成了一张表示该微生物拥有的所有代谢物的代谢网络[[2]](#2)。

##### (1) 通过添加、修改、删除dModel对象中包含的对应微生物的生化反应，可以模拟对微生物所进行的代谢工程上的改造，并且可以对生化反应添加对应的酶动力学方程。

**· modify_reaction(reaction_id, bound_direction, equation)->None**  

  为对应id的反应添加酶动力学方程描述  

    参数：  
    · reaction_id: 需要修改的反应的唯一标识符  
    · bound_direction: 修改的反应上限 和/或 下限(限制为'upper', 'lower', 'both')  
    · equation: 酶动力学方程式，表示该反应的速率，单位以mmol, g, L, h为基础单位，字符串形式(注，此处反应物名称应和之后标注时间导数时的反应物名称相同)
    · is_volume: 描述酶动力学方程式所表示的反应速率是否以体积为基础单位, 若为True, 单位为mmol * L^-1 * h^-1; 反之则为mmol * g^-1 * h^-1, 默认为True

```
Ec.modify_reaction('EX_glc__D_e', 'lower', '-18.5*glc/(0.01+glc)', 1)
```

**· del_reaction(reaction_id)->None**  

  删除已修改的反应  

    参数：  
    · reaction_id：需删除反应的唯一标识符  

```
Ec.del_reaction('EX_glc__D_e')
```

##### (2) 通过修改dModel对象的主优化目标和次级优化目标，可以定量预测微生物生长的反应通量流通情况。

**· change_objective(main_objective, main_objective_direction, sub_objectives, sub_objective_directions, fraction_of_optimum)->None**

  修改dModel对象的主要和次级优化目标

    参数：
    · main_objective：主要优化目标，Reaction类型或Reaction唯一标识符
    · main_objective_direction：主要优化目标的方向，限定为'maximum'或'minimum'
    · sub_objectives：次级优化目标，列表类型，可以包含多个反应或为空
    · sub_objective_directions：次级优化目标的方向，列表类型，一一对应sub_objectives中的反应，列表元素限定为'maximum'或'minimum'
    · fraction_of_optimum：达成主要优化目标值的比例，默认为1，范围为0-1；数值越小，通量平衡优化时将越不偏向主要优化目标而偏向次级优化目标

```
sub = ['EX_glc__D_e', 'EX_o2_e']
sub_dir = ['maximum', 'maximum']
Ec.change_objective('BIOMASS_Ec_iAF1260_core_59p81M', 'maximum', sub, sub_dir, fraction_of_optimum=0.95)
```

##### (3) dModel对象所表示的细胞属性也可进行修改。
细胞属性，比如不同微生物的细胞体积、干重以及洗脱率(死亡率)也会影响到定量分析的数值。可以根据不同微生物的性质对此类参数进行修改以契合实际情况。

**· modify_attribute(volume, weight)->None**

  修改细胞的体积和干重

    参数：
    · volume：细胞体积，单位L，默认数值为1e-15，支持科学计数法输入
    · weight：细胞干重，单位g，默认数值为3e-13，支持科学计数法输入

```
Ec.modify_attribute(2e-15, 1e-13)
```

**· modify_dilution_rate(rate)->None**

  修改细胞的洗脱率

    参数：
    · rate：洗脱率，单位h^-1^，默认数值为0，范围0-1

```
Ec.modify_dilution_rate(0.05)
```

#### 3. 使用求解器对共培养条件进行模拟

```
solver = solver()
model_dict = {'ec1': Ec1, 'ec2': Ec2}
states_dict = {'x_ec1': 0.5, 'x_ec2': 1, 'glc': 10, 'o2': 20}
derivatives = {'ec1':'BIOMASS_Ec_iAF1260_core_59p81M', 'ec2': 'BIOMASS_Ec_iAF1260_core_59p81M', 'o2':'ec1_EX_o2_e+ec2_EX_o2_e', 'glc': 'ec1_EX_glc__D_e+ec2_EX_glc__D_e'}
result = solver.simulate(model_dict, states_dict, derivatives, 5)
```

根据dModel对象，初始物质浓度参数以及时间导数参数使用solver对象的simulate函数进行动态模拟。返回多维数组，包含一系列时间点下的不同物质浓度。

**· simulate(models_dict, states_dict, derivatives_description, times, steps, loopless)->scipy.integrate._ivp.ivp.OdeResult**

  simulate函数对参与反应的dModel代谢网络优化后不断迭代，而整合的酶动力学模型可描述一段时间范围内物质浓度变化情况。在求解微分方程组的同时即可获得细胞浓度以及各种物质浓度的动态变化情况。

    参数：
    · models_dict：参与共培养的所有dModel，字典数据类型，键为给dModel对象取的变量名，值为dModel对象
    · states_dict：参与细胞物质交换反应的反应物，字典数据类型，键为给每种物质取的变量名，值为反应一开始的初始浓度，单位mmol/L（注，每种微生物初始浓度的变量名应命名为x_(dModel变量名，即models_dict中的变量名)，如x_ec)
    · derivatives_description：时间导数，字典数据类型，键为物质的变量名，值为不同微生物参与到对该物质交换的反应通量之和(注，反应通量变量命名按照(model变量名)+_+reaction_id命名，如ec_EX_o2_e)；另外，必须输入微生物的生长通量，键为参与模拟的微生物dModel对象变量，值为对应的生物量反应id
    · times：模拟反应的时长，单位h
    · steps：模拟步数，步数越多模拟结果越精确，但时间消耗更大，默认为100
    · loopless：开启后可以消除FVA算法中包含的通量循环使结果更精确，但开启后时间消耗更大，默认为False

## 参考文献

<p id="1"></p>
[1]  Ebrahim, A., Lerman, J.A., Palsson, B.O., Hyduke, D.R., 2013. COBRApy: COnstraints-Based Reconstruction and Analysis for Python. BMC Syst Biol 7, 74. https://doi.org/10.1186/1752-0509-7-74

<p id="2"></p>
[2]  Kumar, M., Ji, B., Zengler, K., Nielsen, J., 2019. Modelling approaches for studying the microbiome. Nat Microbiol 4, 1253–1267. https://doi.org/10.1038/s41564-019-0491-9
