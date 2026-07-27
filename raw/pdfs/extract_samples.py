import fitz
import os

PDF_DIR = "/home/ubuntu/wiki-foodreg/raw/pdfs"

# Extract a few examples first
for fname in ["weish_2018_10.pdf", "weish_2022_01.pdf", "weish_2023_01.pdf", "weish_2024_06.pdf"]:
    filepath = os.path.join(PDF_DIR, fname)
    doc = fitz.open(filepath)
    print(f"\n{'='*60}")
    print(f"FILE: {fname}  Pages: {len(doc)}")
    print(f"{'='*60}")
    for i in range(len(doc)):
        text = doc[i].get_text()
        print(f"\n--- Page {i+1} ---")
        print(text[:4000])
    doc.close()
