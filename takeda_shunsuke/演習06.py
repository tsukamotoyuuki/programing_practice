print("最大公約数を求めます。二つの数値を入力してください")
x=int(input())
print()
y=int(input())
z=1

while z!=0:
    z=x%y
    x=y
    if z!=0:
        y=z
print("最大公約数は"+str(y)+"です。")
