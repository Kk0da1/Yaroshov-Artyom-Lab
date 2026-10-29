q=[int(input()) for i in range(int(input()))]
w=0
e=10000000000
if len(q)==0:
    print('Нет чисел')
else:
    for i in q:
        if i>w:
            w=i
    for x in q:
        if x<e:
            e=x
    print(len(q), sum(q), w, e,  f'{sum(q)/len(q):.2f}')


