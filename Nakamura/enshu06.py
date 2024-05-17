a = 390
b = 273
if a > b:
    while a % b != 0:
        c = b
        b = a % b
        a = c

print(b)