
# Задача 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
import math

a = int(input('Введите число от 1 до 7 \n'))

if a > 0 and a < 6:
    print(f'{a} является рабочим днем')
elif a == 6 or a == 7:
    print(f'{a} является выходным днем')
else:
    print('введено неверное число')


# Задача 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число x \n'))
y = int(input('Введите число y \n'))
z = int(input('Введите число z \n'))

leftside = not (x or y or z)
rigthside = not x and not y and not z
result = leftside == rigthside

if result == True:
    print('Утверждение истино')
else:
    print('Утверждение ложно')


# Задача 3, Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Задайте число x \n'))

y = int(input('Задайте число y \n'))

if x > 0 and y > 0:
    print('номер четверти - 1')
elif x < 0 and y > 0:
    print('Номер плоскости - 2')
elif x < 0 and y < 0:
    print('Номер плоскости - 3')
elif x > 0 and y < 0:
    print('Номер плоскости - 4')
else:
    print('Точка находится на координатной прямой')

# Задача 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

a = int(input("Введите номер плоскости: от 1 до 4 \n"))

if a == 1:
    print('принимаемые значения: x > 0 and y > 0')
elif a == 2:
    print('принимаемые значения: x < 0 and y > 0')
elif a == 3:
    print('принимаемые значения: x < 0 and y < 0')
elif a == 4:
    print('принимаемые значения: x > 0 and y < 0')
else:
    print('неверно указан номер плоскости')


# Задача 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

Ax = int(input('Введите x точки A \n'))
Ay = int(input('Введите y точки A \n'))
Bx = int(input('Введите x точки B \n'))
By = int(input('Введите y точки B \n'))

firstKatet = (Ax - Bx)**2
secondKatet = (Ay - By)**2
distance = round(math.sqrt(firstKatet + secondKatet), 2)
print(distance)