for i in range(10):
    for j in range(10):
        if i == 0 and j == 0:
            print(" ", end="\t")
        elif i == 0 or j == 0:
            print(i+j, end="\t")
        else:
            print(i*j, end="\t")
    print()