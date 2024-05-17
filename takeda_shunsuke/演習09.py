l=[i for i in range(4000,5001) if i%17 == 0]
print(l)
a=0
while x != len(l):
    print(l[a])
    b=[]
    while l[a] % 2 == 0:
        b.append(2)
        l[a] //= 2
    f=3
    while f * f <= l[a]:
        if l[a] % f == 0:
            b.append(f)
            l[a] //= f
        else:
            f += 2
        if l[a] != 1:
            b.append(l.a)
    a=a+1
