a=int(input('任意の整数を入力:'))

if a%3 != 0 and a%7 != 0 and a%2 != 0 and a%5 != 0:
     print('◎')
elif a%2 != 0 and a%3 == 0 and a%7 != 0:
    print('◎')
elif a%3 == 0 and a%7 == 0 and a%5 == 0:
    print('◎')
elif a%2 == 0 and a%5 == 0:
    print('◎')
else:
    print("×")