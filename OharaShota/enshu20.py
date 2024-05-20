def furui(n):
    prime = [i for i in range(2, n+1)]
    for i in prime:
        for j in range(i * 2, n + 1, i):
            try:
                prime.remove(j)
            except:
                pass
    return prime


prime = furui(10000)
x = -1
for i in prime:
    if i == x + 2:
        print(f"{x} , {i}")
    x = i
