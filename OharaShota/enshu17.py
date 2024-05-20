l = [68, 9, 100, 81]
li = [[" " for i in range(len(l))] for j in range(12)]
for i in range(len(l)):
    li[-1][i] = f"{i+1}"
    li[-2][i] = "="

p = 0
for i in l:
    count = -3
    while i >= 10:
        i -= 10
        li[count][p] = "*"
        count -= 1
    p += 1



for i in li:
    for j in i:
        print(j,end="")
    print()