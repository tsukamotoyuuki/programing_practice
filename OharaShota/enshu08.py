x, y = map(int, input("セール開始日と終了日を入力してください").split())
if 10 <= x <= 15 or 10 <= y <= 15 or x < 10 and 15 < y:
    print("セール期間と工事期間が重なっています")
else:
    print("セール期間と工事期間が重なっていません")
