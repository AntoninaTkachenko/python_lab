
# завдання 1

def circle_area(r):
    return 3.14159 * r * r


def rectangle_area(a, b):
    return a * b


def triangle_area(a, h):
    return a * h / 2


def main():
    figure = input("Фігура: ")

    if figure == "круг":
        r = float(input("Радіус: "))
        print("Площа круга:", circle_area(r))

    elif figure == "прямокутник":
        a = float(input("Ширина: "))
        b = float(input("Висота: "))
        print("Площа прямокутника:", rectangle_area(a, b))

    elif figure == "трикутник":
        a = float(input("Основа: "))
        h = float(input("Висота: "))
        print("Площа трикутника:", triangle_area(a, h))


main()


# завдання 2

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def divisors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result


def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n = n // 10

    return total


def main():
    n = int(input("Введіть число: "))

    if is_prime(n):
        print("Просте число: так")
    else:
        print("Просте число: ні")

    print("Дільники:", divisors(n))
    print("Сума цифр:", digit_sum(n))


main()


# завдання 3

def average(grades):
    return sum(grades) / len(grades)


def minimum(grades):
    return min(grades)


def maximum(grades):
    return max(grades)


def count_above(grades, value):
    count = 0

    for grade in grades:
        if grade > value:
            count += 1

    return count


def main():
    grades = [10, 8, 12, 9, 11]
    value = int(input("Поріг: "))

    print("Середній бал:", average(grades))
    print("Мінімальна:", minimum(grades))
    print("Максимальна:", maximum(grades))
    print("Вище", value, ":", count_above(grades, value))


main()


# завдання 4

def check_length(password):
    return len(password) >= 8


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True

    return False


def check_upper(password):
    for char in password:
        if char.isupper():
            return True

    return False


def check_lower(password):
    for char in password:
        if char.islower():
            return True

    return False


def check_special(password):
    for char in password:
        if not char.isalnum():
            return True

    return False


def validate_password(password):
    errors = []

    if not check_length(password):
        errors.append("довжина менше 8 символів")

    if not check_digit(password):
        errors.append("немає цифри")

    if not check_upper(password):
        errors.append("немає великої літери")

    if not check_lower(password):
        errors.append("немає малої літери")

    if not check_special(password):
        errors.append("немає спеціального символу")

    return len(errors) == 0, errors


def main():
    password = input("Password: ")

    valid, errors = validate_password(password)

    if valid:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано:")

        for error in errors:
            print(error)


main()
