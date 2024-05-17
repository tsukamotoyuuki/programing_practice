target = int(input())
t2 = target % 2
t3 = target % 3
t5 = target % 5
t7 = target % 7

if not t2 and t5:
    print("◎")
elif not t3 and not t5 and not t7:
    print("◎")
elif t2 and not t3 and t7:
    print("◎")
elif t2 and t5 and t7:
    print("◎")
else:
    print("x")