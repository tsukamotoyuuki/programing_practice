l = [68, 9, 100, 81]
count = 1
for i in l:
    ans = ""
    while i >= 10:
        ans = "*" + ans
        i -= 10
    print(f"{count}:{ans}")
    count += 1
    