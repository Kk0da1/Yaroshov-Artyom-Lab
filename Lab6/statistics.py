a=[int(input()) for i in range(int(input()))]
b=0
c=10000000000
if len(a)==0:
    print('Нет чисел')
else:
    for i in a:
        if i>b:
            b=i
    for x in a:
        if x<c:
            c=x
    print(len(a), sum(a), b, c,  f'{sum(a)/len(a):.2f}')


