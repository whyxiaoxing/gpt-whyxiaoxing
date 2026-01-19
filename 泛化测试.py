import matplotlib.pyplot

from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval

def 泛化测试(_JSON模型训练数据:str,_JSON测试集合:str)->None:

    test_json=COCO(_JSON测试集合)
    predict_json=test_json.loadRes(_JSON模型训练数据)

    coco_eval=COCOeval(test_json,predict_json,iouType="bbox") #bbox 是检测模式
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    stats=coco_eval.stats
    result={
        "AP@[0.50:0.95]": float(stats[0]),
        "AP@0.50": float(stats[1]),
        "AP@0.75": float(stats[2]),
        "AP_small": float(stats[3]),
        "AP_medium": float(stats[4]),
        "AP_large": float(stats[5]),
        "AR@1": float(stats[6]),
        "AR@10": float(stats[7]),
        "AR@100": float(stats[8]),
        "AR_small": float(stats[9]),
        "AR_medium": float(stats[10]),
        "AR_large": float(stats[11]),
    }
    # 使用matplotlib展示
    x_name=list(result.keys())
    y_name=[float(result([k]) for k in x_name)]

    matplotlib.pyplot.figure(figsize=(12,5))
    matplotlib.pyplot.bar(x_name,y_name)
    matplotlib.pyplot.yilm(0.0,1.0)
    matplotlib.pyplot.xticks(rotation=45,ha='right')
    matplotlib.pyplot.ylabel("值(0~1)")
    matplotlib.pyplot.title("泛化数据展示")

    for a,b in enumerate(y_name):
        matplotlib.pyplot.text(a,b,"{:.2f}",ha='center',va='bottom',fontsize=10)

    matplotlib.pyplot.tight_layout()
    matplotlib.pyplot.show()
