# 数字から漢数字に変換
def kanjidec(x):
    if x == 0:
        x = ''
    elif x == 1:
        x = '一'
    elif x == 2:
        x = '二'
    elif x == 3:
        x = '三'
    elif x == 4:
        x = '四'
    elif x == 5:
        x = '五'
    elif x == 6:
        x = '六'
    elif x == 7:
        x = '七'
    elif x == 8:
        x = '八'
    elif x == 9:
        x = '九'

    return x


def num2kanji(x):
    # 入力された数字をint型に変換して処理
    x = int(x)
    if x > 200000000:
        print('2億以下の数字を入力してください')
    else:
        # 1億以上の場合の処理
        if x >= 100000000:
            a = x // 100000000
            print(f'{kanjidec(a)}億', end='')
            x %= 100000000

        # 万以上億未満の処理
        if x >= 10000:
            a = x // 10000
            thousanddec(a)
            x %= 10000
            print('万', end='')

        thousanddec(x)


def thousanddec(x):
    if x >= 1000:
        a = x // 1000
        # 千、百、十の値が一の場合は表示しない
        if a != 1:
            print(f'{kanjidec(a)}千', end='')
        else:
            print('千', end='')
        x %= 1000

    if x >= 100:
        a = x // 100
        if a != 1:
            print(f'{kanjidec(a)}百', end='')
        else:
            print('百', end='')
        x %= 100

    if x >= 10:
        a = x // 10
        print(f'{kanjidec(a)}十', end='')
        x %= 10

    print(kanjidec(x), end='')


if __name__ == '__main__':
    n = input('2億以下の数字を入力してください')
    num2kanji(n)
