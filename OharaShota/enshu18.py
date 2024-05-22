import re
path = input("ファイルパスを入力してください")

try:
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
except:
    print("ファイルが読み込めませんでした")
    exit(0)

l = list(s.split())
print(l)

suuji = re.compile("^\d")
moji = re.compile("(\".*\")|(\'.*\')")
