start_day = int(input("セール開始日を入力 : "))
finish_day = int(input("セール終了日を入力 : "))

if finish_day < 10 or 15 < start_day:
    print("大丈夫やで")
else:
    print("あきまへんな")