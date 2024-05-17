x, y = map(int, input().split())
z = x % y

while z != 0:
    x = y
    y = z
    z = x % y

print(y)
