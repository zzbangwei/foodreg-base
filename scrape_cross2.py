#!/usr/bin/env python3
"""Scrape additive-category cross reference with log file."""
import requests
from bs4 import BeautifulSoup
import time
import os
import re
import sys

BASE_URL = "https://gb2760.cfsa.net.cn"
OUT_DIR = os.path.expanduser("~/wiki-foodreg/tables")
LOG_FILE = os.path.expanduser("~/wiki-foodreg/scrape_cross.log")

def log(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(msg + '\n')
    print(msg, flush=True)

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; FoodRegBot/1.0)',
    'Accept': 'text/html,application/xhtml+xml',
})

def fetch(url, timeout=25):
    for attempt in range(3):
        try:
            resp = session.get(url, timeout=timeout)
            resp.encoding = 'utf-8'
            return BeautifulSoup(resp.text, 'lxml')
        except Exception as e:
            if attempt == 2:
                raise
            time.sleep(2)

def make_md_table(headers, data):
    lines = [f"| {' | '.join(headers)} |"]
    lines.append(f"|{'|'.join(['---']*len(headers))}|")
    for row in data:
        escaped = [str(c).replace('|', '\\|').replace('\n', ' ') for c in row]
        lines.append(f"| {' | '.join(escaped)} |")
    return '\n'.join(lines) + '\n'

def scrape_faid_page(faid):
    url = f"{BASE_URL}/addtives/faid/{faid}.html"
    soup = fetch(url, timeout=20)
    tables = soup.find_all('table')
    regulations = []
    for table in tables:
        rows = table.find_all('tr')
        if not rows:
            continue
        headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        if any('食品分类号' in h for h in headers) and any('最大使用量' in h for h in headers):
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

def main():
    # Clear log
    with open(LOG_FILE, 'w') as f:
        f.write('')
    
    log("Reading additive list...")
    add_file = os.path.join(OUT_DIR, 'additive-list.md')
    additives = []
    with open(add_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('|') and not line.startswith('| CNS') and not line.startswith('|---'):
                parts = [p.strip() for p in line.split('|')[1:-1]]
                if len(parts) >= 6 and parts[5].isdigit():
                    additives.append({
                        'cn_name': parts[2],
                        'en_name': parts[3],
                        'cns': parts[0],
                        'ins': parts[1],
                        'func': parts[4],
                        'faid': parts[5],
                    })
    
    log(f"Found {len(additives)} additives to process")
    
    all_rows = []
    errors = []
    start_time = time.time()
    
    for i, add in enumerate(additives):
        faid = add['faid']
        
        try:
            regulations = scrape_faid_page(faid)
            for reg in regulations:
                all_rows.append([
                    add['cn_name'], add['en_name'], add['cns'], add['ins'],
                    add['func'], add['faid'],
                    reg[0], reg[1], reg[2], reg[3],
                ])
        except Exception as e:
            err_msg = f"faid/{faid} ({add['cn_name']}): {e}"
            errors.append(err_msg)
            log(f"  ERROR: {err_msg}")
        
        if (i + 1) % 10 == 0 or (i + 1) == len(additives):
            elapsed = time.time() - start_time
            rate = (i + 1) / elapsed if elapsed > 0 else 0
            eta = (len(additives) - (i + 1)) / rate if rate > 0 else 0
            log(f"  [{i+1}/{len(additives)}] {100*(i+1)/len(additives):.0f}% | "
                f"{len(all_rows)} cross-refs | {rate:.1f}/s | ETA {eta:.0f}s")
        
        time.sleep(0.5)
    
    log(f"\nSaving {len(all_rows)} cross-reference records...")
    with open(os.path.join(OUT_DIR, 'additive-category-cross.md'), 'w') as f:
        f.write(f"# 添加剂-食品分类关联表\n\n")
        f.write(f"来源: {BASE_URL}/addtives/faid/*.html\n")
        f.write(f"关联记录数: {len(all_rows)}\n\n")
        f.write(make_md_table(
            ['添加剂中文名', '添加剂英文名', 'CNS', 'INS', '功能', 'faid',
             '食品分类号', '食品名称', '最大使用量(g/kg)', '备注'],
            all_rows
        ))
    
    if errors:
        log(f"\nErrors ({len(errors)}):")
        for e in errors[:10]:
            log(f"  {e}")
    
    elapsed = time.time() - start_time
    log(f"\nDone! {len(all_rows)} records | Time: {elapsed:.0f}s")
    log(f"Errors: {len(errors)}")

if __name__ == '__main__':
    main()
