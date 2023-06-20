#  # 1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".


def var_assign(var_int, var_float, var_str):
    return var_int, var_float, var_str


# # 2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int.


def multiply_var(var_int):
    big_int = var_int * 3.5
    return big_int


# # 3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу,
# # результат свяжите с той же переменной.


def increase_var(var_float):
    var_float -= 1
    return var_float


# 4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений
# не привязывайте ни к каким переменным.


def division_vars(var_int, var_float, big_int):
    return var_int / var_float, big_int / var_float


# # 5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании
# # нового значения используйте операции конкатенации (+) и повторения строки (*).


def change_value():
    var_str = "No" * 2 + "Yes" * 3
    return var_str
