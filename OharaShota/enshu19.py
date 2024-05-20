x = int(input(), 15)
print(x ** 100)

l = [1]
for i in range(101):
    t = 0
    f = len(l)
    while t < f:
        n = l[t] * x
        k = t
        while n >= 0:
            try:
                l[k] = n % 10
            except:
                l.append(n % 10)
            n //= 10
            k += 1
        t += 1

for i in reversed(l):
    print(i, end="")
