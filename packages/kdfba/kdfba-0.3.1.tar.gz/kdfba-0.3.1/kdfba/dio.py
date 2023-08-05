
### io
## 读取各种文件类型的模型，转化为cobra.Model的子类dModel
###

from pathlib import Path
from dfba.model import dModel
from cobra.io import read_sbml_model
from cobra.io import load_json_model
from cobra.io import load_matlab_model
from cobra.io import load_yaml_model
from cobra import Model
from typing import IO, Match, Optional, Pattern, Tuple, Type, Union
import numpy as np


class dio():

    # 将cobra里的Model类转换成dModel类
    def transfer_model2dModel(
        self,
        model: Model,
    ) -> dModel:
        return dModel(model)

    # 将读取的sbml文件转化为dModel
    def read_sbml_dModel(
        self,
        filename: Union[str, IO, Path],
        number: Type = float,
        **kwargs,
    ) -> dModel:
        return self.transfer_model2dModel(read_sbml_model(filename, number, **kwargs))

    # 将读取的json文件转化为dModel
    def load_json_dModel(self, filename: Union[str, Path, IO]) -> dModel:
        return self.transfer_model2dModel(load_json_model(filename))

    # 将读取的mat文件转化为dModel
    def load_matlab_dModel(
        self,
        infile_path: Union[str, Path, IO],
        variable_name: Optional[str] = None,
        inf: float = np.inf,
    ) -> dModel:
        return self.transfer_model2dModel(load_matlab_model(infile_path, variable_name, inf))

    def load_yaml_dModel(self, filename: Union[str, Path]) -> dModel:
        return self.transfer_model2dModel(load_yaml_model(filename))
