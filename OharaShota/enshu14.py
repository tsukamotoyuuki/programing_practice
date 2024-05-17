import random
rndArray = []
for i in range(32):
    x = random.randint(1,50)
    rndArray.append(x)

print(rndArray)

def mergesort(list):
    if len(list) == 1:
        return list
    mid = len(list) // 2

    left = mergesort(list[:mid])
    right = mergesort(list[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i,j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result

print(mergesort(rndArray))