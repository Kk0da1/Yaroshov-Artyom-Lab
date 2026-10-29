from functions import sum_digits, average, normalize_text

# 1. Сумма цифр
number = int(input("Введите целое число: "))
print("Сумма цифр:", sum_digits(number))


# 2. Среднее списка
raw = input("Введите числа через пробел: ")
numbers = [float(x) for x in raw.split()]
result = average(numbers)
if result is None:
    print("Нет данных")
else:
    print("Среднее:", result)

# 3. Нормализация текста
text = input("Введите произвольный текст: ")
print("Нормализованный текст:", normalize_text(text))

# Индивидуальное задание
from functions import select_numbers

raw = input("Введите целые числа через пробел: ")
numbers = [int(x) for x in raw.split()]
porog = int(input("Введите порог (целое неотрицательное): "))
selected = select_numbers(numbers, porog)
print("Отобранные числа:", selected)
