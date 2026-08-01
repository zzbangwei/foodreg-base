#!/usr/bin/env python3
"""Test scraping structure of CFSA pages."""
import requests
from bs4 import BeautifulSoup

def test_page(url, name):
    print(f"\n{'='*60}")
    print(f"Testing: {name} - {url}")
    print('='*60)
    resp = requests.get(url, timeout=30)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'lxml')
    
    table = soup.find('table')
    if table:
        rows = table.find_all('tr')
        print(f"Found {len(rows)} rows (including header)")
        headers = [th.get_text(strip=True) for th in rows[0].find_all('th')]
        print(f"Headers: {headers}")
        print(f"First row: {[td.get_text(strip=True)[:60] for td in rows[1].find_all('td')]}")
        print(f"Last row: {[td.get_text(strip=True)[:60] for td in rows[-1].find_all('td')]}")
    else:
        print("No table found!")
        # Check if there are multiple tables
        tables = soup.find_all('table')
        print(f"Total tables on page: {len(tables)}")

# Test all main pages
test_page("https://gb2760.cfsa.net.cn/addtives.html", "Additives")
test_page("https://gb2760.cfsa.net.cn/processing.html", "Processing Aids")
test_page("https://gb2760.cfsa.net.cn/enzyme.html", "Enzymes")
test_page("https://gb2760.cfsa.net.cn/category.html", "Category")

# Test a single faid page for usage regulations
test_page("https://gb2760.cfsa.net.cn/addtives/faid/1.html", "FAID 1")

# Test spices pages
test_page("https://gb2760.cfsa.net.cn/spices/type/b2.html", "Natural Flavors B.2")
test_page("https://gb2760.cfsa.net.cn/spices/type/b3.html", "Synthetic Flavors B.3")
