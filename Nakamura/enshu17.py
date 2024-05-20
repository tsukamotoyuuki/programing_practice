import random

l = []
ll = [[0 for i in range(4)]for j in range(10)]

for i in range(4):
    l.append(random.randint(0, 100))

print(l)


for i in range(10):
    for j in range(len(l)):
        if l[j] < 10:
            continue
        else:
            ll[i][j] = 1
            l[j] -= 10


for i in range(10):
    for j in range(len(l)):
        if ll[-i - 1][j] == 1:
            print('*',end='')
        else:
            print(' ', end='')
    print()

for i in range(len(l)):
    print('=', end='')

print()
for i in range(len(l)):
    print(i + 1, end='')
