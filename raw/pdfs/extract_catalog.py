import fitz
import sys

doc = fitz.open("sanxin_catalog.pdf")
print(f"Pages: {len(doc)}", flush=True)

# Print first 5 pages to understand structure
for i in range(min(10, len(doc))):
    text = doc[i].get_text()
    print(f"\n=== Page {i+1} ===", flush=True)
    print(text[:3000], flush=True)
doc.close()
