
# завдання 1

nums = [12, 3, 4, 14, -12, 5, 10, 16, -4]

positive = []
negative = []
even = []
multiple3 = []

for n in nums:
    if n > 0:
        positive.append(n)
    if n < 0:
        negative.append(n)
    if n % 2 == 0:
        even.append(n)
    if n % 3 == 0:
        multiple3.append(n)

print("Додатні:", positive)
print("Від'ємні:", negative)
print("Парні:", even)
print("Кратні 3:", multiple3)
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))
print("Average:", round(sum(nums) / len(nums), 2))


# завдання 2

group1 = {'Anna', 'Ivan', 'Olha'}
group2 = {'Ivan', 'Maksym', 'Olha'}

print("Спільні:", sorted(group1 & group2))
print("Тільки group1:", sorted(group1 - group2))
print("Тільки group2:", sorted(group2 - group1))
print("Усі:", sorted(group1 | group2))


# завдання 3

products = {
    'milk': 48,
    'tea': 75,
    'bread': 35,
    'cheese': 120
}

name = input("Назва товару: ")
price = float(input("Ціна товару: "))
products[name] = price

search = input("Який товар знайти? ")
result = products.get(search)

if result is not None:
    print(search, "—", result, "грн")
else:
    print("Товар не знайдено")

low = float(input("Мінімальна ціна: "))
high = float(input("Максимальна ціна: "))

for name, price in products.items():
    if low <= price <= high:
        print(name, "—", price, "грн")


# завдання 4

group_info = ('10-IT', '2026/2027')

students = {
    'Anna': [10, 11, 12, 9, 10],
    'Ivan': [8, 9, 10, 11, 9]
}

print(group_info[0], "—", group_info[1])

name = input("Введіть ПІБ нового учня: ")
grades = []

for i in range(5):
    grade = int(input("Введіть оцінку від 1 до 12: "))

    while grade < 1 or grade > 12:
        grade = int(input("Помилка! Введіть оцінку від 1 до 12: "))

    grades.append(grade)

students[name] = grades

rating = {}

for name, grades in students.items():
    average = sum(grades) / 5
    rating[name] = average
    print(name, ":", *grades)
    print(name, "—", round(average, 2))

print("Рейтинг:")

for name in sorted(rating, key=rating.get, reverse=True):
    print(name, "—", round(rating[name], 2))

best = max(rating, key=rating.get)

print("Найкращий результат:", best, "—", round(rating[best], 2))
