n = 10000
l = [2]
ll = []

for i in range(3,n):
    for j in range(2,i):
        if i % j == 0:
            break

        if j == i - 1:
            l.append(i)
            if len(l) == 2:
                if l[1] - l[0] == 2:
                    ll.append([l[0],l[1]])
            l[0] = l[1]
            del l[1]

print(ll)