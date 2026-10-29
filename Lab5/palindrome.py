q=input('Введите текст:')
w=''
for i in q:
    if i!=' ':
        w+=i.lower()
if q=="":
    print('Слов нет')
else:
    if w==w[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')
