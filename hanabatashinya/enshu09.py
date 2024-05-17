for x in range(4000, 5001):
    if not(x % 17):
        result = f"{x} = "
        for waru in range(2, 5001):
            kaisu = 0
            amari = x % waru
            while amari == 0:
                kaisu += 1
                amari = x % waru
                if amari == 0:
                    x /= waru
            if kaisu:
                result += f"{waru} ^ {kaisu} * "
        print(result[:-3])


