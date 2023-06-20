# 1. Даны два целых числа A и B (A < B).
# Найти сумму всех целых чисел от A до B включительно.


def sum_of_integers(number_1: int, number_2: int):
    sum_numbers = 0
    for i in range(number_1, number_2 + 1):
        sum_numbers += i
    return sum_numbers


#  2. Найти сумму всех натуральных чисел от A до B


def sum_of_natural_numb(list_natural_numbers: list):
    sum_numbers = 0
    for i in range(len(list_natural_numbers)):
        if list_natural_numbers[i] > 0 and not isinstance(
            list_natural_numbers[i], float
        ):
            sum_numbers += list_natural_numbers[i]
    return sum_numbers


#  3. Найти произведение положительных, сумму и количество
# отрицательных из 10 введенных целых значений


def integer_operations(list_integers_numbers: list):
    multiplication_of_positive_num = 1
    sum_of_negative_num = 0
    count_of_negative_num = 0

    for i in range(len(list_integers_numbers)):
        if list_integers_numbers[i] > 0:
            multiplication_of_positive_num *= list_integers_numbers[i]
        else:
            sum_of_negative_num += list_integers_numbers[i]
            count_of_negative_num += 1
    return multiplication_of_positive_num, sum_of_negative_num, count_of_negative_num


#  4. Дан словарь пловцов с их результатами.
# Напечатать лучший результат заплыва среди 6 участников

# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 3
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17

dict_1 = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}


def best_result(dict_swimmers: dict):
    for key, value in dict_swimmers.items():
        if value == max(dict_swimmers.values()):
            return (
                f"Лучший результат заплыва: {key} - " f"{max(dict_swimmers.values())}"
            )


#  5. Есть массив чисел. Известно, что каждое число в этом массиве
# имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5.
# Напишите программу, которая будет выводить уникальное число

arr_different_int = [1, 2, 1, 9, 2, 9, 5]


def uniq_number(arr_find_uniq: list):
    for i in range(len(arr_find_uniq)):
        if arr_find_uniq.count(arr_find_uniq[i]) == 1:
            return f"Уникальное число списка: {arr_find_uniq[i]}"


print(uniq_number(arr_different_int))
