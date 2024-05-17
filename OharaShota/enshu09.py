for i in range(4012, 5001, 17):
    ans = f"{i} = "
    count = 0
    for j in range(2,300):
        while i % j == 0:
            count += 1
            i /= j
        if count != 0:
            ans += f"{j} ^ {count} * "
        count = 0
    print(ans[:-3])