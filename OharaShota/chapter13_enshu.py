from pathlib import Path
import datetime
import locale
locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")

today = datetime.date.today()
p = Path(F"{today.year:04}{today.month:02}{today.day:02}")
if not p.is_dir():
    p.mkdir()
else:
    print("ディレクトリは既に存在します")

import requests
from bs4 import BeautifulSoup
import re

url = "https://secure.winschool.jp/sozai/IT56/chapter13/sample13_3_2.html"

def save(url):
    responce = requests.get(url)
    responce.encoding = "UTF-8"
    soup = BeautifulSoup(responce.text, "html.parser")
    name = re.search('\w*.html', url)
    with open(F"{p}/{name.group()}", "w", encoding="UTF-8") as f:
        f.write(f"{soup}")
    for a in soup.find_all("a"):
        href = a.get("href")
        save(href)


save(url)