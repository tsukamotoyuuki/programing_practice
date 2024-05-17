x = int(input("整数を入力してください"))
y = int(input("整数を入力してください"))

a = x
b = y

sho = 0
amari = 1

while amari:
    sho = a // b
    amari = a % b
    a = b
    b = amari

print(f"{x}と{y}の最大公約数は{a}です")
