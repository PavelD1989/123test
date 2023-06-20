# Задание 1. Присвойте двум переменным любые числовые значения.
a = 6
b = 7

# Задание 2. Составьте четыре сложных логических выражения с помощью
# оператора and, два из которых должны давать истину, а два других - ложь.
if 4 < a < 10 and 3 < b < 12:
    print(True)
else:
    print(False)

if 0 < a < 23 and 1 < b < 10:
    print(True)
else:
    print(False)

if b < a < -1 and 5 < b < 11:
    print(True)
else:
    print(False)

if 1 < a < 3 and 11 < b < a:
    print(True)
else:
    print(False)


# Задание 3. Составьте четыре сложных логических выражения с помощью
# оператора or, два из которых должны давать истину, а два других - ложь.
if a < b or b < 4:
    print(True)
else:
    print(False)

if 0 < a < b or a < b < 12:
    print(True)
else:
    print(False)

if a > b or b <= 4:
    print(True)
else:
    print(False)

if b < a or 12 < b <= 12:
    print(True)
else:
    print(False)

# Задание 4. Попробуйте использовать в сложных логических выражениях
# работу с переменными строкового типа.
str_1 = 'Строка первая'
str_2 = 'Строка вторая'

if 22 < len(str_1) < 39 and 33 < len(str_2):
    print(True)
else:
    print(False)

if str_1 is str_2 and str_1 is str_2:
    print(True)
else:
    print(False)


