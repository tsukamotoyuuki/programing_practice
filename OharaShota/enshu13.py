import random
rndArray = []
for i in range(30):
    x = random.randint(1,50)
    rndArray.append(x)

print(rndArray)

n=1
for i in range(len(rndArray)):
    for j in range(len(rndArray) - n):
        x = rndArray[j]
        y = rndArray[j+1]
        if x > y:
            rndArray[j+1] = x
            rndArray[j] = y
        print(rndArray)

print(rndArray)