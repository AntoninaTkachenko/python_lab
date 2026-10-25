
# приклад 1

grades = [10, 8, 12, 9, 11]
print("Min:", min(grades))
print("Max:", max(grades))
print("Сума:", sum(grades))
print("Середнє:", sum(grades) / len(grades))


# приклад 2

numbers = [5, 2, 9, 1]
numbers.append(7)
numbers.remove(2)
numbers.sort()
print(numbers)


# приклад 3

numbers = [12, -3, 4, -7, 10, 5]
positive = []

for number in numbers:
    if number > 0:
        positive.append(number)

print(positive)


# приклад 4

point = (15, -4)
x, y = point
print("x:", x)
print("y:", y)


# приклад 5

names = ["Ivan", "Anna", "Ivan", "Olha", "Anna"]
unique_names = set(names)
print(unique_names)


# приклад 6

math = {"Ivan", "Anna", "Olha"}
python = {"Anna", "Maksym", "Ivan"}

print("Спільні:", math & python)
print("Тільки math:", math - python)
print("Усі:", math | python)


# приклад 7

prices = {"bread": 35, "milk": 48}
prices["cheese"] = 120
prices["bread"] = 38
print(prices)


# приклад 8

prices = {"bread": 38, "milk": 48, "cheese": 120}

for product, price in prices.items():
    print(product, "-", price, "грн")


# приклад 9

students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10]
}

print(students["Anna"])


# приклад 10

students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10]
}

for name, grades in students.items():
    average = sum(grades) / len(grades)
    print(name, round(average, 2))


# приклад 11

students = {
    "Anna": [10, 11, 12],
    "Ivan": [8, 9, 10],
    "Olha": [11, 12, 12]
}

best_name = ""
best_average = 0

for name, grades in students.items():
    average = sum(grades) / len(grades)

    if average > best_average:
        best_average = average
        best_name = name

print("Найкращий:", best_name, round(best_average, 2))


# приклад 12

grades = [10, 8, 12]
point = (10, 20)
subjects = {"Python", "HTML", "Python"}
student = {"name": "Ivan", "grade": 11}

print(grades, point, subjects, student)
