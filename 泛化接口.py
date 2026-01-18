from pathlib import Path
import numpy
from numpy.typing import NDArray

def 泛化测试(NMS后数据:NDArray,测试集数据:NDArray) ->None:















def 读取数据集(测试集路径:str)->NDArray | None:
    if 测试集路径 is None or 测试集路径=="":
        raise ValueError("路径为空")
    a=0
    绝对路径=测试集路径+f"{a}.txt"
    缓存list: list[ NDArray[numpy.float32]]=[]

    try:
        while True:

            数据 = Path(绝对路径).read_text(encoding="utf-8")
            数据展开 = numpy.fromstring(数据,sep=" ",dtype=numpy.float32)
            if 数据展开.size == 0:
                a+=1
                continue
            if 数据展开.size %5 !=0:
                raise  ValueError(f"列数不是 5 的倍数：{绝对路径}")
            矩阵=数据展开.resize(-1,5)
            重排=矩阵[:,[1,2,3,4,0]]
            缓存list.append(重排)
            a+=1

    except FileNotFoundError:
        if a<=1:
            raise

        输出: NDArray[numpy.float32]=numpy.vstack(缓存list) if len(缓存list)>0 else numpy.empty((0,5),dtype=numpy.float32)

        return 输出
    except BaseException:
        raise


