#!/usr/bin/env python3
"""Scrape GB 14880 nutrition fortifier cross-reference table.

For each nutrition fortifier, visit its detail page and extract:
  食品名称 | 化合物来源 | 使用量要求 | 来源公告 | 备注
"""

import requests
from bs4 import BeautifulSoup
import time
import os
import sys

BASE_URL = "https://14880.foodvip.net"
OUT_DIR = os.path.expanduser("~/wiki-foodreg/tables")
os.makedirs(OUT_DIR, exist_ok=True)

# All unique itemids from the main page
ITEMIDS = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 78, 79, 81, 82, 83, 84,
    85, 86, 87, 88, 89, 90, 91, 92, 93, 94,
    95, 96, 97, 98, 99, 100, 101, 102, 103, 104,
    105, 106, 107, 108, 109, 110, 111, 112, 113, 114,
    115, 182, 183, 184,
]

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; NutritionBot/1.0)',
    'Accept': 'text/html,application/xhtml+xml',
})

def fetch(url, timeout=25):
    """Fetch a URL with retries."""
    for attempt in range(3):
        try:
            resp = session.get(url, timeout=timeout)
            resp.encoding = 'utf-8'
            return BeautifulSoup(resp.text, 'lxml')
        except Exception as e:
            if attempt == 2:
                raise
            print(f"  Retry {attempt+1}: {e}")
            time.sleep(2)

def scrape_detail(itemid):
    """Scrape detail page for one nutrition fortifier."""
    url = f"{BASE_URL}/index/supple/show?itemid={itemid}"
    try:
        soup = fetch(url, timeout=20)
    except Exception as e:
        print(f"  ❌ Failed: itemid={itemid}: {e}")
        return None, []

    # Extract fortifier name from the summary table
    name = ""
    compound_source_summary = ""
    scope = ""
    remark_summary = ""

    tables = soup.find_all('table')
    
    # First table is info table (营养强化剂 | 化合物来源 | 应用范围 | 备注)
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            th = row.find('th')
            if th and len(cells) >= 1:
                label = th.get_text(strip=True)
                cell_text = cells[0].get_text(strip=True)
                if '营养强化剂' in label:
                    name = cell_text
                elif '化合物来源' in label:
                    compound_source_summary = cell_text
                elif '应用范围' in label:
                    scope = cell_text
                elif '备注' in label:
                    remark_summary = cell_text

    # Find the usage table (食品名称 | 化合物来源 | 使用量要求 | 来源 | 备注)
    usage_rows = []
    for table in tables:
        rows = table.find_all('tr')
        if not rows:
            continue
        # Check header
        headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        if '食品名称' in headers and '使用量要求' in headers:
            for row in rows[1:]:
                cells = row.find_all('td')
                if len(cells) >= 5:
                    food_name = cells[0].get_text(strip=True)
                    compound = cells[1].get_text(strip=True)
                    usage = cells[2].get_text(strip=True)
                    source = cells[3].get_text(strip=True)
                    remark = cells[4].get_text(strip=True) if len(cells) > 4 else ""
                    if food_name:
                        usage_rows.append([food_name, compound, usage, source, remark])

    return {
        'name': name,
        'compound_source_summary': compound_source_summary,
        'scope': scope,
        'remark_summary': remark_summary,
        'itemid': itemid,
    }, usage_rows

def make_md_table(headers, data):
    """Create a markdown table."""
    if not data:
        lines = [f"| {' | '.join(headers)} |"]
        lines.append(f"|{'|'.join(['---']*len(headers))}|")
        return '\n'.join(lines) + '\n'
    
    lines = [f"| {' | '.join(headers)} |"]
    lines.append(f"|{'|'.join(['---']*len(headers))}|")
    for row in data:
        escaped = [str(c).replace('|', '\\|').replace('\n', ' ') for c in row]
        lines.append(f"| {' | '.join(escaped)} |")
    return '\n'.join(lines) + '\n'

def main():
    print(f"Scraping {len(ITEMIDS)} nutrition fortifier detail pages...")
    print(f"Base URL: {BASE_URL}/index/supple/show?itemid=XX")
    print()

    all_rows = []
    errors = []
    processed = 0
    start_time = time.time()

    for i, itemid in enumerate(ITEMIDS):
        try:
            info, usage_rows = scrape_detail(itemid)
            name = info['name'] if info else f"itemid={itemid}"
            scope = info.get('scope', '') if info else ''
            
            if usage_rows:
                for row in usage_rows:
                    all_rows.append([
                        name,
                        row[1] if row[1] else info.get('compound_source_summary', ''),
                        row[0],  # 食品名称
                        row[2],  # 使用量要求
                        row[3],  # 来源公告
                        row[4],  # 备注
                        scope,
                    ])
            else:
                # No usage rows - might be a fortifier with only summary
                all_rows.append([
                    name,
                    info.get('compound_source_summary', '') if info else '',
                    '[无具体食品类别]',
                    '[见标准正文]',
                    '-',
                    info.get('remark_summary', '') if info else '',
                    scope,
                ])
        except Exception as e:
            err_msg = f"itemid={itemid}: {e}"
            errors.append(err_msg)
            print(f"  ❌ {err_msg}")

        processed += 1
        if processed % 10 == 0 or processed == len(ITEMIDS):
            elapsed = time.time() - start_time
            rate = processed / elapsed if elapsed > 0 else 0
            eta = (len(ITEMIDS) - processed) / rate if rate > 0 else 0
            print(f"  [{processed}/{len(ITEMIDS)}] {100*processed/len(ITEMIDS):.0f}% | "
                  f"{len(all_rows)} cross-refs | {rate:.1f}/s | ETA {eta:.0f}s")

        time.sleep(0.3)  # Be polite

    # Save
    out_path = os.path.join(OUT_DIR, 'nutrition-fortifier-category-cross.md')
    
    actual_fortifiers = len(set(row[0] for row in all_rows))
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("# GB 14880-2012 营养强化剂×食品类别使用量关联表\n\n")
        f.write(f"## 数据来源\n")
        f.write(f"- **标准**: GB 14880-2012 食品安全国家标准 食品营养强化剂使用标准\n")
        f.write(f"- **网站**: {BASE_URL}/index/supple/index\n")
        f.write(f"- **爬取日期**: 2026-06-23\n")
        f.write(f"- **营养强化剂条目**: {len(ITEMIDS)}（含普通食品和特殊膳食用食品分别列出）\n")
        f.write(f"- **去重营养强化剂**: ~{actual_fortifiers} 种\n")
        f.write(f"- **关联记录总数**: {len(all_rows)}\n\n")
        f.write("---\n\n")

        f.write("## 关联表\n\n")
        f.write(make_md_table(
            ['营养强化剂', '化合物来源', '食品类别', '使用量要求', '来源公告', '备注', '适用范围'],
            all_rows
        ))

    print(f"\n✅ Saved {len(all_rows)} cross-reference records to {out_path}")
    
    if errors:
        print(f"\n⚠️  Errors ({len(errors)}):")
        for e in errors[:20]:
            print(f"  {e}")

    elapsed = time.time() - start_time
    print(f"\nDone in {elapsed:.0f}s")

if __name__ == '__main__':
    main()
