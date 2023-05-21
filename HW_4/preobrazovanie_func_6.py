# 1. Перевести строку в массив "Robin Singh" => ["Robin”, “Singh"],
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]


def str_to_massive(string: str) -> list:
    return string.split()


#  2. Дан список: [‘Ivan’, ‘Ivanov’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanov! Добро пожаловать в Minsk Belarus”


def text_with_data_of_person(name: list, city: str, country: str):
    data = f"Привет, {name[0]} {name[1]}! Добро пожаловать в {city} {country}"
    return data


# 3. Дан список, сделайте из него строку.


def make_str(orig_list: list):
    return " ".join(orig_list)


#  4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое
# значение, удалите элемент из списка под индексом 6


def add_pop_list(value: str, orig_list: list):
    orig_list.insert(2, value)
    orig_list.pop(5)
    return orig_list


#  5. Есть 2 словаря. Необходимо их объединить по ключам, а значения
# ключей поместить в список, если у одного словаря есть ключ "а", а у другого
# нет, то поставить значение None на соответствующую позицию(1-я позиция для
# 1-ого словаря, вторая для 2-ого) // Решение спросил подсмотрел у Дмитрия.
# ab = {'a': [1, None], 'b': [2, None],
# 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}


def merging_dictionaries(dict_1: dict, dict_2: dict, result_dict: dict):
    for key, value in dict_1.items():
        if key in dict_2:
            result_dict[key] = [dict_1[key], dict_2[key]]
        else:
            result_dict[key] = [value, None]

    for key, value in dict_2.items():
        if key in dict_1:
            result_dict[key] = [dict_1[key], dict_2[key]]
        else:
            result_dict[key] = [None, value]

    return
