# x = int(input(), 15)
# print(x ** 100)
#
# l = [1]
# for i in range(101):
#     t = 0
#     f = len(l)
#     while t < f:
#         n = l[t] * x
#         k = t
#         while n >= 0:
#             try:
#                 l[k] = n % 10
#             except:
#                 l.append(n % 10)
#             n //= 10
#             k += 1
#         t += 1
#
# for i in reversed(l):
#     print(i, end="")

N = 10 # N乗
x = int(input(), 15)
print(x ** N)

ReNumLi = [1]
for i in range(N):
    over = 0
    for j in range(len(ReNumLi)):
        tmp = ReNumLi[j] * x + over
        ReNumLi[j] = tmp % 10
        over = tmp // 10

    while over > 0:
        ReNumLi.append(over % 10)
        over //= 10

for i in reversed(ReNumLi):
    print(i, end="")




