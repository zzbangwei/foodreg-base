import fitz
import os
import json

PDF_DIR = "/home/ubuntu/wiki-foodreg/raw/pdfs"

announcements = {
    "2018-10": {"file": "weish_2018_10.pdf", "title": "黑果腺肋花楸果等2种新食品原料"},
    "2022-01": {"file": "weish_2022_01.pdf", "title": "关山樱花等2种新食品原料"},
    "2022-02": {"file": "weish_2022_02.pdf", "title": "莱茵衣藻等3种新食品原料"},
    "2023-01": {"file": "weish_2023_01.pdf", "title": "假肠膜明串珠菌等1种新食品原料"},
    "2023-03": {"file": "weish_2023_03.pdf", "title": "蓝莓花色苷等2种新食品原料"},
    "2023-05": {"file": "weish_2023_05.pdf", "title": "文冠果种仁等2种新食品原料"},
    "2024-03": {"file": "weish_2024_03.pdf", "title": "阿拉伯木聚糖等3种新食品原料"},
    "2024-05": {"file": "weish_2024_05.pdf", "title": "拟微球藻油等2种新食品原料"},
    "2024-06": {"file": "weish_2024_06.pdf", "title": "金花茶培养物等1种新食品原料"},
    "2025-01": {"file": "weish_2025_01.pdf", "title": "甜叶菊多酚等5种新食品原料"},
    "2025-03": {"file": "weish_2025_03.pdf", "title": "樱花多酚等2种新食品原料"},
    "2025-04": {"file": "weish_2025_04.pdf", "title": "D-阿洛酮糖等5种新食品原料"},
}

for key, info in announcements.items():
    filepath = os.path.join(PDF_DIR, info["file"])
    doc = fitz.open(filepath)
    all_text = ""
    for page in doc:
        all_text += page.get_text() + "\n"
    doc.close()
    
    outpath = os.path.join(PDF_DIR, f"{key}_text.txt")
    with open(outpath, 'w', encoding='utf-8') as f:
        f.write(all_text)
    print(f"OK {key}: {len(all_text)} chars -> {outpath}")
