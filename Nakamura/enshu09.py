for i in range(4000, 5000):

    # 17で割り切れる場合のみ素因数分解
    if i % 17 == 0:
        print(f'{i} = ', end='')
        k = i

        # 素因数分解開始
        for j in range(2, i):

            # 割り切れる場合に割り切れる数の表示
            if k % j == 0:
                print(j, end='')
                k = k / j
                n = 1

                # 同じ数で割り切れるか判定し、累乗計算
                if k % j == 0:
                    while k % j == 0:
                        n += 1
                        k /= j

                # 累乗があった場合は累乗数の表示
                if n >= 2:
                    print(f' ^ {n}', end='')

                # まだほかの数字で割れる場合は続行
                if k != 1:
                    print(' * ', end='')
                else:
                    print()
                    break
