import fitz
import os
import re
import json

PDF_DIR = "/home/ubuntu/wiki-foodreg/raw/pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

# Map: announcement -> (pdf_url, output_filename)
announcements = {
    "2018-10": ("https://www.nhc.gov.cn/sps/c100088/201809/ab14ac31ac644f74b64f2d5795d75d84/files/1743489820246_60607.pdf", "weish_2018_10.pdf"),
    "2022-01": ("https://www.nhc.gov.cn/sps/c100088/202203/b83fe875f3734cc28ecdb93c1f01a1c7/files/1734002818839_41671.pdf", "weish_2022_01.pdf"),
    "2022-02": ("https://www.nhc.gov.cn/sps/c100088/202205/404e6b3007b14917a96a298b906fa372/files/1734002801144_58520.pdf", "weish_2022_02.pdf"),
    "2023-01": ("https://www.nhc.gov.cn/wjw/c100175/202303/7245722850bc42a4b2228b5d408ad29a/files/1734002813655_25876.pdf", "weish_2023_01.pdf"),
    "2023-03": ("https://www.nhc.gov.cn/sps/c100088/202305/6f0bd372a8f74e6dbbaaaaa267379790/files/1734002775708_77056.pdf", "weish_2023_03.pdf"),
    "2023-05": ("https://www.nhc.gov.cn/sps/c100088/202308/605e444048824d5cbb550eaa0648eb49/files/1734002769817_96850.pdf", "weish_2023_05.pdf"),
    "2024-03": ("https://www.nhc.gov.cn/sps/c100088/202408/e290d4ef552940d4b50b1846cba92e6f/files/1743489829005_12155.pdf", "weish_2024_03.pdf"),
    "2024-05": ("https://www.nhc.gov.cn/wjw/c100175/202410/553ebf82dcf1421c942cf4c54bc32790/files/1739860172879_47366.pdf", "weish_2024_05.pdf"),
    "2024-06": ("https://www.nhc.gov.cn/sps/c100088/202412/ccde2b21bdb8482c9aa08ee54ac775eb/files/1736390721427_73537.pdf", "weish_2024_06.pdf"),
    "2025-01": ("https://www.nhc.gov.cn/sps/c100088/202502/943dcc40bc45486cbcda67859bf1fddb/files/1741760236048_98505.pdf", "weish_2025_01.pdf"),
    "2025-03": ("https://www.nhc.gov.cn/sps/c100088/202505/c3f86f8a80b34251892cf040bb4b218e/files/1746697805401_88471.pdf", "weish_2025_03.pdf"),
    "2025-04": ("https://www.nhc.gov.cn/sps/c100088/202507/63194b55e9fd4a6daa74f59a06cfd792/files/D-%E9%98%BF%E6%B4%9B%E9%85%AE%E7%B3%96%E7%AD%895%E7%A7%8D%E6%96%B0%E9%A3%9F%E5%93%81%E5%8E%9F%E6%96%99.pdf", "weish_2025_04.pdf"),
}

for key, (url, fname) in announcements.items():
    filepath = os.path.join(PDF_DIR, fname)
    if os.path.exists(filepath):
        print(f"SKIP {key} - already exists: {filepath}")
        continue
    import urllib.request
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=30).read()
        with open(filepath, 'wb') as f:
            f.write(data)
        print(f"OK {key} -> {filepath} ({len(data)} bytes)")
    except Exception as e:
        print(f"FAIL {key}: {e}")
