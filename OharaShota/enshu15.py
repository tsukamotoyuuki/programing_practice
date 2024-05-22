import random
rndArray = []
for i in range(32):
    x = random.randint(1,50)
    rndArray.append(x)

list_ki = []
ans = []

def nibungi(list, n):
    if len(list) == 3:
        if n < list[1]:
            nibungi(list[0],n)
        else:
            nibungi(list[1],n)
    else:
        list = [[], n, []]


def heapsort(list):
    for i in list:
        nibungi(list_ki, i)
    return list_ki

def printh(list):
    if len(list[0]) == 0:
        ans.append(list[1])
    else:
        printh(list[0])

    if len(list[2]) != 0:
        printh(list)

def heap(list):
    list = heapsort(list)
    print(list)
    # printh(list)
    # print(ans)

heap(rndArray)