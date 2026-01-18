import numpy
from numpy.typing import NDArray

def 泛化测试(NMS后数据:NDArray,测试集数据:NDArray) ->None:















def 读取数据集(测试集路径:str)->NDArray | None:
    if 测试集路径 is None or 测试集路径=="":
        raise ValueError("路径为空")
    a=0
    绝对路径=测试集路径+f"{a}.txt"

    try:
        while True:

             with open(绝对路径) as r:

    except FileNotFoundError:
        return None
