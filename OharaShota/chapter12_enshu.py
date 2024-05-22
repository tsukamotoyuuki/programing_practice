import os
from pathlib import Path
import time
import datetime
import locale
locale.setlocale(locale.LC_ALL, "ja_JP.UTF-8")

today = datetime.date.today()
p = Path(F"{today.year:04}{today.month:02}{today.day:02}")
if not p.is_dir():
    p.mkdir()
else:
    print("ディレクトリは既に存在します")

y, m, d = map(int,input("年/月/日  ").split("/"))
date = datetime.date(y, m, d)
print(f"{date}は{date.strftime('%a')}曜日")
dd = datetime.timedelta(weeks=2)
print(F"{date}の二週間後は{date + dd}")