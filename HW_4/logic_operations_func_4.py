#  1. Присвойте двум переменным любые числовые значения.

# # 2. Составьте четыре сложных логических выражения с помощью
# # # оператора and, два из которых должны давать истину, а два других - ложь.


def difficult_expressions1(a, b):
    if 4 < a < 10 and 3 < b < 12:
        print(True)
    else:
        print(False)


def difficult_expressions2(a, b):
    if 0 < a < 23 and 1 < b < 10:
        print(True)
    else:
        print(False)


def difficult_expression3(a, b):
    if b < a < -1 and 5 < b < 11:
        print(True)
    else:
        print(False)


def difficult_expressions4(a, b):
    if 1 < a < 3 and 11 < b < a:
        print(True)
    else:
        print(False)


# 3. Составьте четыре сложных логических выражения с помощью
# # # # оператора or, два из которых должны давать истину, а два других - ложь.\

def difficult_expressions_or_1(a: int, b: int):
    if a < b or b < 4:
        print(True)
    else:
        print(False)


def difficult_expressions_or_2(a, b):
    if (0 < a < b) or (a < b < 12):
        print(True)
    else:
        print(False)


def difficult_expressions_or_3(a: int, b: int):
    if a > b or b <= 4:
        print(True)
    else:
        print(False)


def difficult_expressions_or_4(a: int, b: int):
    if b < a or 12 < b <= 12:
        print(True)
    else:
        print(False)


#  4. Попробуйте использовать в сложных логических выражениях
# # работу с переменными строкового типа.
# str_1 = 'Строка первая'
# str_2 = 'Строка вторая'


def difficult_logic_operations(str_1, str_2):
    if 22 < len(str_1) < 39 and 33 < len(str_2):
        print(True)
    else:
        print(False)
    if str_1 is str_2 and str_1 is str_2:
        print(True)
    else:
        print(False)
