# 1 Привести к целому типу -1.6, 2.99


def convert_to_int(num_a):
    """
    :param num_a: исходное число для перевода в целочисленное
    :return: преобразование float в int

    """

    return int(num_a)


# # 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'


def replace_character(str_a, char_old, char_new):
    """
    :param str_a: исходная строка
    :param char_old: заменяемый символ
    :param char_new: символ замены
    :return: функция замены символа в строке
    """

    return str_a.replace(char_old, char_new)


#
# # 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’


def add_to_string(str_a: str, str_b: str) -> str:
    """
    :type str_b: str
    :param str_a: исходная строка
    :param str_b: добавляемая строка
    :return: соединение строк
    """
    return str_a + str_b


# 4. Изменение положения слов в строке из 2-х слов


def changing_place_2words(str_a: str) -> str:
    """
    :param str_a: исходная строка
    :return: вывод новой строки после изменения порядка
    """
    return str_a.split(" ")[1] + " " + str_a.split(" ")[0]


# 5 Удаление пробелов в начале и конце строки
def remove_begin_and_end_spaces(str_a1: str) -> str:
    """
    :type str_a1: str
    :param str_a1: строка с начальными и конечными пробелами
    :return: строка без начальных и конечных пробелов
    """
    return str_a1.strip()


#  6. Добавление в школу очередного ученического класса


def add_student_group(name: dict, class_letter: str, students: int) -> dict:
    """
    :type name: dict
    :type class_letter: str
    :param name: имя словаря
    :param class_letter: ученический класс
    :param students: количество учеников в классе
    :return: вывод словаря с добавленной новой записью
    """
    name[class_letter] = students  # Добавление в словарь новой записи
    return name


# 7. Извлечение из списка n-го элемента
def extract_element(user_arr: list, element: int):
    """
    :param user_arr: список
    :param element: номер элемента
    :return: отображение искомого элемента списка
    """
    if element <= len(user_arr):
        return user_arr[element]
    else:
        return (
            f"Номер запрашиваемого элемента списка '{element}' "
            f"больше количества элементов списка"
        )


#  8. Вывести входит ли строка1 в строку2 (пример: employ и employment)
def include_str(orig_string: str, string_for_search: str) -> bool:
    """
    :param orig_string: str
    :param string_for_search: str
    :return: вывод true -если одна строка входит во вторую, вывод false -если первая строка не входит во вторую
    """

    if orig_string.find(string_for_search) == -1:
        return False
    else:
        return True


#  9. Вывести нужные символы из строки "My name is Agent Smith"


def char_output_1(string_a: str, index: int) -> str:
    """
    :param string_a: str
    :param index: index
    :return: вывод нужных символов из строки
    """

    return string_a[index]


# Задание 10. Вывод уникального числа из массива


def unique_number_from_array(given_arr: list):
    """
    :param given_arr:list
    :return: вывод уникального символа из массива
    """

    for i in range(len(given_arr)):
        if given_arr.count(given_arr[i]) == 1:
            return given_arr[i]
