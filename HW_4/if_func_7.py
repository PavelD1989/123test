# 1.Дано целое число. Если оно является положительным, то прибавить к нему 1; в противном случае не изменять его.
# # Вывести полученное число.

def int_val(a_int):
    if a_int > 0:
        a_int = a_int + 1
        return a_int
    else:
        return a_int


# #2. Даны три целых числа. Найти количество положительных чисел в исходном наборе.

def how_much_positive_numbers(list_1: list):
    count_positive = 0
    for i in range(len(list_1)):
         if list_1[i] > 0:
            count_positive += 1
    return count_positive


# 3. Дан номер года (положительное целое число). Определить количество
# дней в этом году, учитывая, что обычный год насчитывает 365 дней,
# а високосный — 366 дней. Високосным считается год, делящийся на 4,
# за исключением тех годов, которые делятся на 100 и не делятся на 400
# (например, годы 300, 1300 и 1900 не являются високосными, а 1200 и 2000
# являются).


def days_the_year(the_year):
    if the_year % 4 != 0:
        return f"В {the_year} году 365 дней"
    elif the_year % 100 != 0:
        return f"В {the_year} году 366 дней"
    elif the_year % 400 != 0:
        return f"В {the_year} году 365 дней"
    else:
        return f"В {the_year} году 366 дней"


#  4. Дано целое число в диапазоне 1–7. Вывести строку — название дня  недели, соответствующее данному числу
# (1 — «понедельник», 2 — «вторник» и т. д.)


def day_of_week(day_number: int):
    if day_number == 1:
        return "понедельник"
    elif day_number == 2:
        return "вторник"
    elif day_number == 3:
        return "среда"
    elif day_number == 4:
        return "четверг"
    elif day_number == 5:
        return "пятница"
    elif day_number == 6:
        return "суббота"
    elif day_number == 7:
        return "воскресенье"


# 5. Единицы массы пронумерованы следующим образом: 1 — килограмм,
# 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы
# (целое число в диапазоне 1–5) и масса тела в этих единицах (вещественное
# число). Найти массу тела в килограммах.


def mass_in_kg(unit_of_mass, body_mass):
    if unit_of_mass == 1:
        return ("Масса тела в килограммах:", body_mass)
    elif unit_of_mass == 2:
        return ("Масса тела в миллиграммах:", body_mass * 1000000)
    elif unit_of_mass == 3:
        return ("Масса тела в граммах:", body_mass * 1000)
    elif unit_of_mass == 4:
        return ("Масса тела в тоннах:", body_mass / 1000)
    elif unit_of_mass == 5:
        return ("Масса тела в центнерах:", body_mass / 100)
    else:
        return "В условиях задачи такой единицы массы не задано"

