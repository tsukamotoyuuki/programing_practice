def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    return l


l = [2, 5, 3, 1, 6]

print(bubblesort(l))