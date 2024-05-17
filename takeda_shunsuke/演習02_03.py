print(end='\t')
for x in[1,2,3,4,5,6,7,8,9]:
    print(x,end='\t')
print()

for i in[1,2,3,4,5,6,7,8,9]:
    print(i,end='\t')
    for j in [1,2,3,4,5,6,7,8,9]:
        p=i*j
        if p%6==0:
            print('##',end='\t')
        elif p%3==0:
            print('@@',end='\t')
        elif p%2==0:
            print('**',end='\t')
        else:
            print(p, end='\t')
    print()

