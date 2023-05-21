# 1
def len_str(string: str):
    list_of_string = list(string)
    list_of_string.pop(0)
    list_of_string.pop()
    list_of_string.pop(2)
    list_of_string.pop(-2)
    return len(list_of_string)


# 2
def str_extraction(string_abc: str):
    # первые восемь
    o_1 = string_abc[0:8]
    # четыре центральных символа
    o_2 = string_abc[int(len(string_a) / 2 - 1): int(len(string_a) / 2 + 3)]
    # символы с индексами кратными трем
    o_3 = string_abc[2: int(len(string_a)): 3]
    # перевернуть строку
    o_4 = string_abc[::-1]
    return o_1, o_2, o_3, o_4


# 3
def insert_name(original_string: str, substring_to_replace: str, name: str):
    return original_string.replace(substring_to_replace, name).replace(
        name, substring_to_replace, 1)


# 4
def work_with_string(work_string: str, sub_str: str):
    o_1 = work_string.find("Hello")  # 0
    o_2 = work_string.find("e")  # 1
    o_3 = work_string.find("w") + 1
    o_4 = work_string.count("l")

    if work_string.find("Hello") == 0:
        o_5 = "Строка начинается с подстроки 'Hello'"
    else:
        o_5 = "Строка не начинается с подстроки 'Hello'"

    if work_string.find(sub_str, len(work_string) - len(sub_str), len(work_string)) != -1:
        o_6 = f"Строка оканчивается на подстроку '{sub_str}'"
    else:
        o_6 = f"Строка не оканчивается на подстроку '{sub_str}'"

    return o_1, o_2, o_3, o_4, o_5, o_6
