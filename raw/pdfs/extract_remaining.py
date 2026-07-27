import fitz
import os
import re

PDF_DIR = "/home/ubuntu/wiki-foodreg/raw/pdfs"

# Extract all remaining PDFs
remaining = [
    "weish_2023_03.pdf", "weish_2023_05.pdf", "weish_2024_03.pdf",
    "weish_2024_05.pdf", "weish_2025_01.pdf", "weish_2025_03.pdf", "weish_2025_04.pdf"
]

for fname in remaining:
    filepath = os.path.join(PDF_DIR, fname)
    doc = fitz.open(filepath)
    print(f"\n{'='*60}")
    print(f"FILE: {fname}  Pages: {len(doc)}")
    print(f"{'='*60}")
    # Only print first 3 pages for structure analysis
    for i in range(min(3, len(doc))):
        text = doc[i].get_text()
        print(f"\n--- Page {i+1} ---")
        print(text[:3000])
    doc.close()
