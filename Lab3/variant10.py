q=int(input('Введите коэффициент загрузки:'))
if 0<=q<=4:
    print('Начало')
elif 5<=q<=94:
    print('Загрузка')
elif 95<=q<=100:
    print('Завершение')
else:
    print('Ошибка')
