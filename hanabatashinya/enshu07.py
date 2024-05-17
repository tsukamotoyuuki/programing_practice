target = int(input(""))

t2 = target % 2
t3 = target % 3
t5 = target % 5
t7 = target % 7

if (t2 == 0) and t5:
    print("@")
elif (t3 == 0) and (t5 == 0) and (t7 == 0):
    print("@")
elif t2 and (t3 == 0) and t7:
    print("@")
elif t2 and t5 and t7:
    print("@")
else:
    print("//")