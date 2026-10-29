a=[int(input()) for i in range(int(input()))]
if len(a)==0:
    print('Нет данных')
else:
    b = [i for i, f in enumerate(a) if f ==max(a)]
print(b)