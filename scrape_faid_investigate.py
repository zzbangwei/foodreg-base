#!/usr/bin/env python3
"""Investigate FAID page structure for usage regulations."""
import requests
from bs4 import BeautifulSoup

url = "https://gb2760.cfsa.net.cn/addtives/faid/1.html"
resp = requests.get(url, timeout=30)
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text, 'lxml')

# Print all tables
tables = soup.find_all('table')
print(f"Total tables: {len(tables)}")
for i, table in enumerate(tables):
    rows = table.find_all('tr')
    print(f"\n--- Table {i}: {len(rows)} rows ---")
    headers = [th.get_text(strip=True)[:50] for th in rows[0].find_all('th')]
    print(f"Headers: {headers}")
    for j, row in enumerate(rows[1:4]):
        cells = [td.get_text(strip=True)[:80] for td in row.find_all('td')]
        print(f"  Row {j+1}: {cells}")

# Also print the page text around key areas
print("\n\n=== Full page text (first 2000 chars) ===")
print(soup.get_text()[:2000])

# Let's check another faid page with more usage data
print("\n\n=== FAID 10 (benzoic acid) ===")
url2 = "https://gb2760.cfsa.net.cn/addtives/faid/10.html"
resp2 = requests.get(url2, timeout=30)
resp2.encoding = 'utf-8'
soup2 = BeautifulSoup(resp2.text, 'lxml')
tables2 = soup2.find_all('table')
print(f"Total tables: {len(tables2)}")
for i, table in enumerate(tables2):
    rows = table.find_all('tr')
    print(f"\n--- Table {i}: {len(rows)} rows ---")
    headers = [th.get_text(strip=True)[:50] for th in rows[0].find_all('th')]
    print(f"Headers: {headers}")
    for j, row in enumerate(rows[1:5]):
        cells = [td.get_text(strip=True)[:80] for td in row.find_all('td')]
        print(f"  Row {j+1}: {cells}")
    if len(rows) > 6:
        print(f"  ... and {len(rows)-6} more data rows")
