import random
rndArray = []
for i in range(30):
    x = random.randint(1,50)
    rndArray.append(x)

print(rndArray)

sortArray = []
while len(rndArray) != 0:
    x = rndArray[0]
    for i in rndArray:
        x = min(x, i)
    sortArray.append(x)
    rndArray.remove(x)

print(sortArray)
