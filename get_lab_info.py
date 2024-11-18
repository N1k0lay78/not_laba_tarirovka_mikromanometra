from datetime import datetime
from docxtpl import InlineImage
import yaml

from eval_Spr import eval_Spr
from laba import get_table, eval_mean_k, save_image

def load_title_info():
    with open('config.yaml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data["document"]


def get_lab_info(doc):
    info = load_title_info()
    info["date_post"] = datetime.now().strftime('%d.%m.%Y')
    info["year"] = datetime.now().strftime('%Y')
    info["Spr"] = f"{round(eval_Spr(), 3)}"
    info["student"] = info["student"] + "\t"
    info["date_get"] = info["date_get"] + "\t"
    info["data"] = get_table()
    info["mean_k"] = eval_mean_k()
    save_image()
    info["plot"] = InlineImage(doc, "plot.png")
    info["scheme"] = InlineImage(doc, "scheme.png")
    return info
