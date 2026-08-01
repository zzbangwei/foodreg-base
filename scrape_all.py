#!/usr/bin/env python3
"""Master scraper for CFSA website GB2760-2024 data.
Produces 7 tables in ~/wiki-foodreg/tables/:
  1. category-list.md
  2. additive-list.md
  3. processing-aid-list.md
  4. enzyme-list.md
  5. natural-flavor-list.md
  6. synthetic-flavor-list.md
  7. additive-category-cross.md
"""
import requests
from bs4 import BeautifulSoup
import time
import os
import re
from collections import OrderedDict

BASE_URL = "https://gb2760.cfsa.net.cn"
OUT_DIR = os.path.expanduser("~/wiki-foodreg/tables")
os.makedirs(OUT_DIR, exist_ok=True)

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; FoodRegBot/1.0)',
    'Accept': 'text/html,application/xhtml+xml',
})

def fetch(url, timeout=30):
    """Fetch a URL with retries."""
    for attempt in range(3):
        try:
            resp = session.get(url, timeout=timeout)
            resp.encoding = 'utf-8'
            return BeautifulSoup(resp.text, 'lxml')
        except Exception as e:
            if attempt == 2:
                raise
            print(f"  Retry {attempt+1} for {url}: {e}")
            time.sleep(2)

def extract_table_rows(soup, table_index=0):
    """Extract rows from a table in soup."""
    tables = soup.find_all('table')
    if not tables or table_index >= len(tables):
        return [], []
    table = tables[table_index]
    rows = table.find_all('tr')
    if not rows:
        return [], []
    headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
    data = []
    for row in rows[1:]:
        cells = row.find_all('td')
        data.append([td.get_text(strip=True) for td in cells])
    return headers, data

def extract_links_from_table(soup, table_index=0, col_idx=0):
    """Extract links from a specific column of the table."""
    tables = soup.find_all('table')
    if not tables or table_index >= len(tables):
        return []
    table = tables[table_index]
    links = []
    for row in table.find_all('tr')[1:]:  # skip header
        cells = row.find_all('td')
        if len(cells) > col_idx:
            a = cells[col_idx].find('a')
            if a:
                links.append((a.get_text(strip=True), a.get('href')))
    return links

def faid_from_href(href):
    """Extract faid number from href like /addtives/faid/123.html"""
    m = re.search(r'/faid/(\d+)\.html', href)
    return int(m.group(1)) if m else None

def make_md_table(headers, data, col_aligns=None):
    """Create a markdown table string."""
    if not data:
        return f"| {' | '.join(headers)} |\n|{'|'.join(['---']*len(headers))}|\n"
    lines = [f"| {' | '.join(headers)} |"]
    if col_aligns:
        lines.append(f"|{'|'.join(col_aligns)}|")
    else:
        lines.append(f"|{'|'.join(['---']*len(headers))}|")
    for row in data:
        # Escape pipes in cells
        escaped = [str(c).replace('|', '\\|').replace('\n', ' ') for c in row]
        lines.append(f"| {' | '.join(escaped)} |")
    return '\n'.join(lines) + '\n'

# ============================================================
# TABLE 1: 食品分类表 (category-list.md)
# ============================================================
def scrape_categories():
    print("\n📋 Scraping food categories...")
    soup = fetch(f"{BASE_URL}/category.html")
    headers, data = extract_table_rows(soup, 0)
    
    # Add hierarchy level
    out_data = []
    for row in data:
        cat_id = row[0].strip() if len(row) > 0 else ''
        cat_name = row[1].strip() if len(row) > 1 else ''
        # Calculate level by dots in category id
        level = cat_id.count('.') + 1 if re.match(r'^\d', cat_id) else 1
        if not re.match(r'^\d', cat_id):
            level = 1
        out_data.append([cat_id, cat_name, str(level)])
    
    with open(os.path.join(OUT_DIR, 'category-list.md'), 'w') as f:
        f.write(f"# 食品分类表\n\n")
        f.write(f"来源: {BASE_URL}/category.html\n")
        f.write(f"记录数: {len(out_data)}\n\n")
        f.write(make_md_table(['食品分类号', '食品类别名称', '层级'], out_data))
    print(f"  ✅ {len(out_data)} categories saved")

# ============================================================
# TABLE 2: 食品添加剂表 (additive-list.md)
# ============================================================
def scrape_additives():
    print("\n📋 Scraping food additives base list...")
    soup = fetch(f"{BASE_URL}/addtives.html")
    
    tables = soup.find_all('table')
    table = tables[0]
    rows = table.find_all('tr')
    headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
    
    additives = []
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) >= 5:
            a_tag = cells[0].find('a')
            href = a_tag.get('href') if a_tag else ''
            faid = faid_from_href(href) if href else ''
            
            cn_name = cells[0].get_text(strip=True)
            en_name = cells[1].get_text(strip=True)
            cns = cells[2].get_text(strip=True)
            ins = cells[3].get_text(strip=True)
            func = cells[4].get_text(strip=True)
            
            additives.append({
                'cn_name': cn_name,
                'en_name': en_name,
                'cns': cns,
                'ins': ins,
                'func': func,
                'faid': str(faid) if faid else '',
            })
    
    out_data = [[a['cns'], a['ins'], a['cn_name'], a['en_name'], a['func'], a['faid']] for a in additives]
    
    with open(os.path.join(OUT_DIR, 'additive-list.md'), 'w') as f:
        f.write(f"# 食品添加剂表\n\n")
        f.write(f"来源: {BASE_URL}/addtives.html\n")
        f.write(f"记录数: {len(out_data)}\n\n")
        f.write(make_md_table(['CNS', 'INS', '中文名', '英文名', '功能', 'faid'], out_data))
    print(f"  ✅ {len(out_data)} additives saved")
    return additives

# ============================================================
# TABLE 3: 加工助剂表 (processing-aid-list.md)
# ============================================================
def scrape_processing_aids():
    print("\n📋 Scraping processing aids...")
    soup = fetch(f"{BASE_URL}/processing.html")
    headers, data = extract_table_rows(soup, 0)
    
    with open(os.path.join(OUT_DIR, 'processing-aid-list.md'), 'w') as f:
        f.write(f"# 加工助剂表\n\n")
        f.write(f"来源: {BASE_URL}/processing.html\n")
        f.write(f"记录数: {len(data)}\n\n")
        f.write(make_md_table(['中文名', '英文名', '功能', '使用范围'], data))
    print(f"  ✅ {len(data)} processing aids saved")

# ============================================================
# TABLE 4: 酶制剂表 (enzyme-list.md)
# ============================================================
def scrape_enzymes():
    print("\n📋 Scraping enzymes...")
    soup = fetch(f"{BASE_URL}/enzyme.html")
    headers, data = extract_table_rows(soup, 0)
    
    with open(os.path.join(OUT_DIR, 'enzyme-list.md'), 'w') as f:
        f.write(f"# 酶制剂表\n\n")
        f.write(f"来源: {BASE_URL}/enzyme.html\n")
        f.write(f"记录数: {len(data)}\n\n")
        f.write(make_md_table(['中文名', '英文名', '来源', '供体', '备注'], data))
    print(f"  ✅ {len(data)} enzymes saved")

# ============================================================
# TABLES 5&6: 香料表
# ============================================================
def scrape_flavors():
    print("\n📋 Scraping flavors...")
    
    # Natural flavors (B.2)
    soup = fetch(f"{BASE_URL}/spices/type/b2.html")
    headers, data = extract_table_rows(soup, 0)
    
    with open(os.path.join(OUT_DIR, 'natural-flavor-list.md'), 'w') as f:
        f.write(f"# 食品用天然香料表 (B.2)\n\n")
        f.write(f"来源: {BASE_URL}/spices/type/b2.html\n")
        f.write(f"记录数: {len(data)}\n\n")
        f.write(make_md_table(['分类', '中文名称', '英文名称', '编码', 'FEMA编码', '分类表', '备注'], data))
    print(f"  ✅ {len(data)} natural flavors saved")
    
    # Synthetic flavors (B.3)
    soup = fetch(f"{BASE_URL}/spices/type/b3.html")
    headers, data = extract_table_rows(soup, 0)
    
    with open(os.path.join(OUT_DIR, 'synthetic-flavor-list.md'), 'w') as f:
        f.write(f"# 食品用合成香料表 (B.3)\n\n")
        f.write(f"来源: {BASE_URL}/spices/type/b3.html\n")
        f.write(f"记录数: {len(data)}\n\n")
        f.write(make_md_table(['分类', '中文名称', '英文名称', '编码', 'FEMA编码', '分类表', '备注'], data))
    print(f"  ✅ {len(data)} synthetic flavors saved")

# ============================================================
# TABLE 7: 添加剂-食品分类关联表
# ============================================================
def scrape_faid_page(faid):
    """Scrape a single faid page for usage regulations."""
    url = f"{BASE_URL}/addtives/faid/{faid}.html"
    try:
        soup = fetch(url, timeout=20)
    except Exception as e:
        print(f"    ❌ Failed to fetch faid/{faid}: {e}")
        return []
    
    tables = soup.find_all('table')
    regulations = []
    
    for table in tables:
        rows = table.find_all('tr')
        if not rows:
            continue
        headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        # Look for the usage table with correct headers
        if '食品分类号' in headers and '最大使用量' in headers:
            for row in rows[1:]:
                cells = row.find_all('td')
                if len(cells) >= 4:
                    cat_id = cells[0].get_text(strip=True)
                    cat_name = cells[1].get_text(strip=True)
                    max_use = cells[2].get_text(strip=True)
                    remark = cells[3].get_text(strip=True)
                    if cat_id and cat_name:
                        regulations.append([cat_id, cat_name, max_use, remark])
    
    return regulations

def scrape_additive_cross(additives):
    """Scrape usage regulations for each additive."""
    print(f"\n📋 Scraping additive-category cross references for {len(additives)} additives...")
    print("  (This will take a few minutes with 0.5s delay between requests)")
    
    all_rows = []
    total = len(additives)
    
    for i, add in enumerate(additives):
        faid = add['faid']
        if not faid:
            continue
        
        if (i + 1) % 20 == 0:
            print(f"  Progress: {i+1}/{total} ({100*(i+1)/total:.0f}%)")
        
        try:
            regulations = scrape_faid_page(faid)
            for reg in regulations:
                all_rows.append([
                    add['cn_name'],
                    add['en_name'],
                    add['cns'],
                    add['ins'],
                    add['func'],
                    add['faid'],
                    reg[0],  # 食品分类号
                    reg[1],  # 食品名称
                    reg[2],  # 最大使用量
                    reg[3],  # 备注
                ])
        except Exception as e:
            print(f"    ❌ Error on faid/{faid} ({add['cn_name']}): {e}")
        
        time.sleep(0.5)  # Be polite to the server
    
    with open(os.path.join(OUT_DIR, 'additive-category-cross.md'), 'w') as f:
        f.write(f"# 添加剂-食品分类关联表\n\n")
        f.write(f"来源: {BASE_URL}/addtives/faid/*.html\n")
        f.write(f"关联记录数: {len(all_rows)}\n\n")
        f.write(make_md_table(
            ['添加剂中文名', '添加剂英文名', 'CNS', 'INS', '功能', 'faid',
             '食品分类号', '食品名称', '最大使用量(g/kg)', '备注'],
            all_rows
        ))
    print(f"  ✅ {len(all_rows)} cross-reference records saved")

# ============================================================
# MAIN
# ============================================================
def main():
    print("=" * 60)
    print("CFSA GB2760-2024 Data Scraper")
    print("=" * 60)
    
    # Step 1: Base tables (fast, independent)
    scrape_categories()
    additives = scrape_additives()
    scrape_processing_aids()
    scrape_enzymes()
    scrape_flavors()
    
    # Step 2: Cross-reference table (slow, 290 requests)
    scrape_additive_cross(additives)
    
    print("\n" + "=" * 60)
    print("All done! Tables saved to ~/wiki-foodreg/tables/")
    print("=" * 60)
    
    # List all files
    for f in sorted(os.listdir(OUT_DIR)):
        size = os.path.getsize(os.path.join(OUT_DIR, f))
        print(f"  {f} ({size:,} bytes)")

if __name__ == '__main__':
    main()
