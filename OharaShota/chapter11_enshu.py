with open("enshu.txt", "w") as f:
    for i in range(10):
        f.write(str(i + 1) + "\n")

ans = 0
with open("enshu.txt", "r") as f:
    for i in f:
        ans += int(i)
print(ans)

import csv

with open("a.csv", "r") as f:
    cin = csv.DictReader(f)
    i, ave = 0, 0
    for row in cin:
        ave += int(row["age"])
        i += 1
    print(F"{ave / i:.3}")

import json

with open("c.json", "r") as f:
    people = json.load(f)
    i, ave = 0, 0
    for person in people:
        ave += int(person["age"])
        i += 1
    print(F"{ave / i:.3}")



