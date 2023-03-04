#  1. Cоздайте словарь, связав его с переменной our_school,
# и наполните его данными, которые бы отражали количество учащихся
# в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.))

our_school = {
    '1a': 20,
    '2б': 18,
    '3в': 23,
    '4г': 21,
    '5а': 20,
    '6б': 19,
    '7в': 24,
    '8г': 22,
    '9а': 25,
    '10а': 24,
}


# Задание 2. Узнайте сколько человек в каком-нибудь классе.


def pupils_count(
    number_of_class: str, our_school: dict
):  # словарь добавляется в переменную 'our_school'  при вызове функции)
    return our_school[number_of_class]


# # 3. Представьте, что в школе произошли изменения,
# # внесите их в словарь:
# # - в трех классах изменилось количество учащихся;
# # - в школе появилось два новых класса;
# # - в школе расформировали один из классов.


# изменить количество учащихся
def pupils_change(number_of_class: str, count_students: int, our_school: dict):
    class_count = our_school[number_of_class] = count_students
    return class_count


# добавление нового класса
def add_our_school_classes(number_of_class: str, count_students: int, our_school: dict):
    new_class = our_school[number_of_class] = count_students
    return new_class


# расформирование класса
def delete_class(number_of_class: str, our_school: dict):
    return our_school.pop(number_of_class)
