l1 = ["", "十", "百", "千"]
l2 = ["", "",  "二", "三", "四", "五", "六", "七", "八", "九"]

n = int(input())
man = True
oku = True
count = 0
if n == 0:
    print("零")
ans = ""
while n != 0:
    count += 1
    x = n%10
    if x != 0:
        if 5 <= count <= 8 and man:
            ans = "万" + ans
            man = False
        elif 9 <= count <= 12 and oku:
            ans = "億" + ans
            oku = False
        if x == 1:
            if count % 4 == 1:
                ans = "一" + ans
            else:
                ans = l1[(count - 1)%4] + ans
        else:
            ans = l2[x] + l1[(count - 1)%4] + ans
    n //= 10
print(ans)