
# Завдання 1

text = input("Введіть текст: ")

letters = 0
digits = 0
spaces = 0
vowels = 0
vowel_list = "аеєиіїоуюяaeiou"

for char in text:
    if char.isalpha():
        letters += 1
    if char.isdigit():
        digits += 1
    if char == " ":
        spaces += 1
    if char.lower() in vowel_list:
        vowels += 1

words = text.split()

print("Символів:", len(text))
print("Літер:", letters)
print("Цифр:", digits)
print("Пробілів:", spaces)
print("Голосних:", vowels)
print("Слів:", len(words))


# Завдання 2

name = input("Введіть прізвище, ім'я та по батькові: ")

parts = name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    first_name = parts[1].capitalize()
    patronymic = parts[2].capitalize()

    result = surname + " " + first_name[0] + "." + patronymic[0] + "."
    print(result)
else:
    print("Потрібно ввести рівно три слова")


# Завдання 3

text1 = input("Перший рядок: ")
text2 = input("Другий рядок: ")

a = text1.lower().replace(" ", "")
b = text2.lower().replace(" ", "")

print("Перший рядок:", a)
print("Другий рядок:", b)

if sorted(a) == sorted(b):
    print("Рядки є анаграмами.")
else:
    print("Рядки не є анаграмами.")


# Завдання 4

sentence = input("Введіть речення: ")

words = sentence.split()

if len(words) > 0:
    longest_len = len(words[0])
    shortest_len = len(words[0])

    for word in words:
        if len(word) > longest_len:
            longest_len = len(word)
        if len(word) < shortest_len:
            shortest_len = len(word)

    print("Найдовші:", end=" ")
    for word in words:
        if len(word) == longest_len:
            print(word, end=" ")
    print()

    print("Найкоротші:", end=" ")
    for word in words:
        if len(word) == shortest_len:
            print(word, end=" ")
    print()

    unique = []

    for word in words:
        if word.lower() not in unique:
            unique.append(word.lower())

    print("Унікальних слів:", len(unique))

    old_word = input("Слово для заміни: ")
    new_word = input("Нове слово: ")

    result = sentence.replace(old_word, new_word)
    print("Після заміни:", result)
else:
    print("Речення порожнє")
