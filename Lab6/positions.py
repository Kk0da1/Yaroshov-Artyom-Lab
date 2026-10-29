q=[int(input()) for i in range(int(input()))]
if len(q)==0:
    print('Нет данных')
else:
    w = [i for i, f in enumerate(q) if f ==max(q)]
print(w)
