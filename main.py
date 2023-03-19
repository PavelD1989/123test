from HW_3.hw3_func import (
    convert_to_int,
    char_output_1,
    add_to_string,
    unique_number_from_array,
    include_str,
    extract_element,
    add_student_group,
    remove_begin_and_end_spaces,
    replace_character,
    changing_place_2words,
)

from HW_4.work_with_var_func_1 import (
    var_assign,
    change_value,
    division_vars,
    increase_var,
    multiply_var,
)

from HW_4.str_func_2 import len_str, str_extraction, insert_name, work_with_string

from HW_4.list_func_3 import (
    two_lists,
    extract_second_element,
    change_last_element,
    link_two_lists,
    few_elements,
    add_new_element,
    return_common_elements,
    unique_elements,
)

from HW_4.logic_operations_func_4 import (
    difficult_expressions1,
    difficult_expressions2,
    difficult_expression3,
    difficult_expressions4,
    difficult_expressions_or_1,
    difficult_expressions_or_2,
    difficult_expressions_or_3,
    difficult_expressions_or_4,
    difficult_logic_operations,
)

from HW_4.dictionaries_func_5 import (
    pupils_count,
    pupils_change,
    add_our_school_classes,
    delete_class,
)

from HW_4.preobrazovanie_func_6 import (
    str_to_massive,
    text_with_data_of_person,
    make_str,
    add_pop_list,
    merging_dictionaries,
)

from HW_4.if_func_7 import (
    int_val,
    how_much_positive_numbers,
    days_the_year,
    day_of_week,
    mass_in_kg,
)

from HW_4.for_func_8 import (
    sum_of_integers,
    sum_of_natural_numb,
    integer_operations,
    best_result,
)

from HW_4.while_func_9 import (
    products_of_number,
    sort_of_flowers,
    summ_of_number_after_segmentation,
    find_grandfather_and_grandson_old,
)

from HW_6.HW_6_file_with_tasks import (
    output_from_file,
    even_and_odd_numbers,
    squares_of_real_numbers,
    swap_file_contents,
)

# __________________________________________________________
# HW_3
# 1
print(convert_to_int(-1.6))
print(convert_to_int(2.99))

# 2
str_a = "www.my_site.com#about"
char_old = "#"
char_new = "/"
print(replace_character(str_a, char_old, char_new))

# 3
str_a = "stroka"
string_for_search = "ing"
print(add_to_string(str_a, string_for_search))

# 4
str_a = "Ivanov Ivan"
print(changing_place_2words(str_a))

# 5
str_a1 = " Мама мыла мылом раму "
print(remove_begin_and_end_spaces(str_a1))

# 6
school = {}
add_student_group(school, "1а", 21)
add_student_group(school, "2а", 20)
add_student_group(school, "3а", 25)
add_student_group(school, "4а", 23)
add_student_group(school, "5а", 22)
add_student_group(school, "6а", 21)
add_student_group(school, "7а", 24)
add_student_group(school, "8а", 27)
add_student_group(school, "9а", 22)
add_student_group(school, "10а", 25)
print(f"Школьные классы: {school}")

# 7
user_arr = ["стол", "стул", "кровать", "шкаф"]
print(extract_element(user_arr, 1))

# 8
orig_string = "employment"
string_for_search = "employ"
print(include_str(orig_string, string_for_search))

# 9.1
string_a = "My name is Agent Smith"
index = 1
print(char_output_1(string_a, index))


# 10
given_arr = [1, 5, 2, 9, 2, 9, 1]
print(unique_number_from_array(given_arr))

# ____________________________________________________________________________________________

# HW_4

# __________
# work_with_var_func_1
# ___________
# 1
var_int = 10
var_float = 8.4
var_string = "No"
print(var_assign(var_int, var_float, var_string))

# 2
print(multiply_var(10))

# 3

print(increase_var(20))


# 4

print(division_vars(2, 3, 4))

# 5

print(change_value())


# ____________
# str_func_2
# _______________
# 1
str_a = "Не менее 8 символов"
print(len_str(str_a))

# 2
str_abc = "абвгдеёжзийклм"
print(str_extraction(str_abc))

# 3
original_string = "my name is name"
substring_to_replace = "name"
name = "Pavel"
print(insert_name(original_string, substring_to_replace, name))


# 4
work_string = "Hello world!"
sub_str = "qwe"
print(work_with_string(work_string, sub_str))

# __________________
# list_func_3
# ____________________
# 1
print(two_lists())


# 2
print(extract_second_element())


# 3
print(change_last_element())


# 4
print(link_two_lists())


# 5
print(few_elements())


# 6
print(add_new_element())


# 7
print(return_common_elements())


# 8
print(unique_elements())


# _____________
# logic_operations_func_4
# ____________
# 1-3
a = 3
b = 4
difficult_expressions1(a, b)
difficult_expressions2(a, b)
difficult_expression3(a, b)
difficult_expressions4(a, b)
difficult_expressions_or_1(a, b)
difficult_expressions_or_2(a, b)
difficult_expressions_or_3(a, b)
difficult_expressions_or_4(a, b)

#  4
str_1 = "Строка первая"
str_2 = "Строка вторая"
difficult_logic_operations(str_1, str_2)
# _________________
# dictionaries_func_5.
# __________________
# 1
our_school = {
    "1a": 20,
    "2б": 18,
    "3в": 23,
    "4г": 21,
    "5а": 20,
    "6б": 19,
    "7в": 24,
    "8г": 22,
    "9а": 25,
    "10а": 24,
}
# 2

print(pupils_count("3в", our_school))

# 3
print(pupils_change("4г", 33, our_school))
print(add_our_school_classes("11a", 22, our_school))
print(delete_class("9a", our_school))


# ___________________
# preobrazovanie_func_6
# ___________________

# 1
str_a = "Robin Singh"
string_b = "I love arrays they are my favorite"
print(str_to_massive(str_a))
print(str_to_massive(string_b))

# 2
name = ["Ivan", "Ivanov"]
city = "Minsk"
country = "Belarus"
print(text_with_data_of_person(name, city, country))

# 3
orig_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(make_str(orig_list))

# 4
orig_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
value = "123"
print(add_pop_list(value, orig_list))


# 5
a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
c = {}
print(merging_dictionaries(a, b, c))

# ______________
# if_func_7
# _________________
# 1

a_int = 10
print(int_val(a_int))

# 2
list_1 = [-3, 5, 7]
print(f"Количество положительных чисел: {how_much_positive_numbers(list_1)}")

# 3
the_year = 2024
print(days_the_year(the_year))

# 4
day_number = 3
print(day_of_week(day_number))

# .5
unit_of_mass = 4
body_mass = 5
print(mass_in_kg(unit_of_mass, body_mass))
# _______________

# for_func_8
# _____________

# 1

number_1 = 3
number_2 = 7

print(
    f"Сумма целых чисел от {a} до {b} включительно: {sum_of_integers(number_1, number_2)}"
)

# 2
list_natural_numbers = [1, -3, 2, 2.2, 3, 4.1]
print(f"Сумма всех натуральных чисел: {sum_of_natural_numb(list_natural_numbers)}")

# 3
list_integers_numbers = [1, -2, -3, -4, 5, 6, 7, 8, 9, -10]
integer_operations(list_integers_numbers)
print(
    f"Произведение положительных чисел: {integer_operations(list_integers_numbers)[0]}"
)
print(f"Сумма отрицательных чисел: {integer_operations(list_integers_numbers)[1]}")
print(f"Количество отрицательных чисел: {integer_operations(list_integers_numbers)[2]}")


# 4
dict_swimmers = {
    "Бекиш Александр": 21.07,
    "Будник Алексей": 20.34,
    "Гребень Анастасия": 22.12,
    "Давидович Татьяна": 30,
    "Дешук Дмитрий": 24.01,
    "Казак Анна": 28.17,
}
print(best_result(dict_swimmers))

# 5
# Повтор 10-ого задания (3ДЗ)

# ___________
# while_func_9
# ______________
# 1
n = 23
print(f"Произведение всех чисел от 0 до {n} = {products_of_number(n)}")

# 2
s_1 = 10
s_2 = 15
print(
    f"Через {sort_of_flowers(s_1, s_2)} лет площадь первых сортов "
    f"будет составлять меньше 10% от площади вторых сортов"
)

# 3
n = 123
print(
    f"Сумма цифр = {summ_of_number_after_segmentation(n)[0]}\nКоличество цифр ="
    f" {summ_of_number_after_segmentation(n)[1]}"
)

# 4
find_grandfather_and_grandson_old()


# HW_6

# 1
print(output_from_file("file1.txt"))

# 2
print(even_and_odd_numbers("file2.txt"))

# 3
print(squares_of_real_numbers("file3.txt"))

# 4
print(swap_file_contents("first.dat", "asdasda", "second.dat", "zxcxc"))
