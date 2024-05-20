path = input("ファイルパスを入力してください")
try:
    with open(path) as f:
        s = f.read()
except:
    print("ファイルが読み込めませんでした")
    exit(0)

l = list(s.split())
print(l)




