import random

l = []
for i in range(4):
    l.append(random.randint(0, 100))

print(l)

for i in range(len(l)):
    print(f'{i + 1} :', end='')

    for j in range(1, 11):
        if l[i] < 10:
            break
        else:
            print('*',end='')
            l[i] -= 10

    print()
