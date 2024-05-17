for i in range(0,10):
    for j in range(0,10):
        if (i == 0) and (j == 0):
            print(" ", end="\t")
        elif i == 0:
            print(j, end="\t")
        elif j == 0:
            print(i, end="\t")
        else:
            result = i*j
            if result % 6 == 0:
                print("##", end="\t")
            elif result % 3 == 0:
                print("@@", end="\t")
            elif result % 2 == 0:
                print("**", end="\t")
            else:
                print(result, end="\t")
    print()