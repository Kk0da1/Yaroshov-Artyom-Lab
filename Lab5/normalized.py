text = input("Введите строку: ")
normalized = ' '.join(text.split())
words = normalized.split() if normalized else []
print(f"Исходная длина: {len(text)}")
print(f"Новая длина: {len(normalized)}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {len(words)}")