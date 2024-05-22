x = int(input(), 15)
print(x ** 100)

l = [1]
for i in range(100):
    t = 0
    for j in range(len(l)):
        n = l[j] * x + t
        l[j] = n % 10
        t = n // 10
    while t > 0:
        l.append(t % 10)
        t //= 10

for i in reversed(l):
    print(i, end="")
