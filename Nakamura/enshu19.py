n = input('4桁の15進数(0~9,A~E)を入力してください')
a = []
b = 0

for i in range(len(n)):
    if n[i] == '0':
        a.append(0)
    elif n[i] == '1':
        a.append(1)
    elif n[i] == '2':
        a.append(2)
    elif n[i] == '3':
        a.append(3)
    elif n[i] == '4':
        a.append(4)
    elif n[i] == '5':
        a.append(5)
    elif n[i] == '6':
        a.append(6)
    elif n[i] == '7':
        a.append(7)
    elif n[i] == '8':
        a.append(8)
    elif n[i] == '9':
        a.append(9)
    elif n[i] == 'A':
        a.append(10)
    elif n[i] == 'B':
        a.append(11)
    elif n[i] == 'C':
        a.append(12)
    elif n[i] == 'D':
        a.append(13)
    elif n[i] == 'E':
        a.append(14)
    else:
        print('指定された文字で入力してください')
        break

for i in range(len(a)):
    b = b + a[i] * 15 ** (len(a) - 1 - i)

c = 1
for i in range(100):
    c = c * b

print(c)