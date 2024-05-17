l = [1, 5, 3, 6, 5, 4, 1, 0, 10, 90, 36, 25, 24]
ll = []

while True:
    min = l[0]
    minnum = 0
    for i in range(len(l)):
        if min > l[i]:
            min = l[i]
            minnum = i

    ll.append(min)
    del l[minnum]

    if l == []:
        break

print(ll)
