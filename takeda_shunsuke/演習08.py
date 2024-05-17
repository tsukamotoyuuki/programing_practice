def check(x):
    return len(x) != len(set(x))

a=int(input('開始日を入力:'))
print()
b=int(input('終了日を入力:'))

l=[i for i in range(a,b+1)]
print(l)
ll = [10,11,12,13,14,15]
suml= l+ll
print(suml)

c=check(suml)

if c == True:
    print("日にちが被っています。考え直してください")
else:
    print("工事との重複はありません。")
