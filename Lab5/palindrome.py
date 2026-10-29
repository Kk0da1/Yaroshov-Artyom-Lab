a=input('Введите текст:')
c=''
for i in a:
    if i!=' ':
        c+=i.lower()
if a=="":
    print('Слов нет')
else:
    if c==c[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')