
# print("Консольный калькулятор")
# print('Для завершения введите "! "')

# while True:
#     num = input("Введите первое число: ")

#     if num == "!":
#         print("Завершено.")
#         break

#     if not num.isdigit():
#         print("Ошибка: введите число.")
#         continue

#     num = int(num)

#     num2 = input("Введите второе число: ")

#     if num2 == "!":
#         print("Завершено.")
#         break

#     if not num2.isdigit():
#         print("Ошибка: введите число.")
#         continue

#     num2 = int(num2)

#     operation = input("Введите операцию: ")

#     if operation == "!":
#         print("Завершено.")
#         break

#     if operation not in ("/", "*", "+", "-"):
#         print("Ошибка: неизвестная операция.")
#         continue

#     if operation == "/" and num2 == 0:
#         print("Деление на ноль невозможно.")
#         continue

#     if operation == "+":
#         result = num + num2
#     elif operation == "-":
#         result = num - num2
#     elif operation == "*":
#         result = num * num2
#     else:
#         result = num / num2

#     print("Результат:", result)






def pal(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]


def f(s):
    w = s.lower().split()
    d = {}

    for x in w:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    return d

#pal()
print(pal("топот"))
print(pal("Не палиндром"))
print(pal("Эскендер Исметович"))


#f()
print(f("мышка мышка клавиатура"))
print(f("Шишкин К С мтуси худший худший преподаватель"))
print(f("один два три два один два"))
