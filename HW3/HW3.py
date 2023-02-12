# 1 Привести к целому типу -1.6, 2.99

num_a = -1.6
num_a_int = int(num_a)
print(num_a_int)

num_b = 2.99
num_b_int = int(num_b)
print(num_b_int)

# 2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

str_a = 'www.my_site.com#about'
result_str_a = str_a.replace("#", "/", 1)
print(result_str_a)

# 3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
str_1str = 'stroka'
str_2str = 'ing'
str_summ = str_1str + str_2str
print(str_summ)

# или с помощью метода .join
vowels = ['stroka', 'ing']
vowels_str = "".join(vowels)
print(vowels_str)

# 4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

str_a = "Ivan Ivanou"
str_summ = str_a[5:11] + " " + str_a[0:4]
print(str_summ)

# 5 Напишите программу которая удаляет пробел в начале, в конце строки

string_1 = " Пример предложения без пробелов "
string_2 = string_1.strip()
print(string_2)

# 6 Создайте словарь, связав его с переменной school, и наполните его данными
# которые бы отражали количество учащихся в десяти разных классах
# (например, 1а, 1б, 2б, 6а, 7в и т.д.).

school = {"1а": 21, "2б": 22, "3в": 23, "4а": 24, "5б": 25, "6a": 26, "7б": 27,
          "8в": 28, "9г": 29, "10a": 30}
print(school)

# 7 Создайте список и извлеките из него списка второй элемент.

example_of_list = [1, 'string ABC', [2, 'EFD']]
a_second_element = example_of_list[1]
print(a_second_element)

# 8 Вывести входит ли строка1 в строку2 (пример: employ и employment )

a_str = "employ"
b_str = "employment"
val_include_or_not = a_str in b_str
if val_include_or_not is True:
    print("Строка '", a_str, "' входит в строку '", b_str, "'")
else:
    print("Строка '", a_str, "' не входит в строку '", b_str, "'")

# 9 Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt

x = "My name is Agent Smith"
print(x[1])
print(x[3:-6:3])

# 10* Есть массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

arr_a = [1, 5, 2, 9, 2, 9, 1]

for i in range(len(arr_a)):
    if 1 == arr_a.count(arr_a[i]):
        print("Уникальное число списка: ", arr_a[i])

# Задание 1.3
# 1) x = 17 / 2 * 3 + 2
# 2) x = 2 + 17 / 2 * 3
# 3) x = 19 % 4 + 15 / 2 * 3
# 4) x = (15 + 6) - 10 * 4
# 5) x = 17 / 2 % 2 * 3**3

print(17 / 2 * 3 + 2)
print(2 + 17 / 2 * 3)
print(19 % 4 + 15 / 2 * 3)
print((15 + 6) - 10 * 4)
print(17 / 2 % 2 * 3 ** 3)

# Задание 1.4
# Создать три переменные, содержащие возраст трех
# ближайших соседей, найти сумму и вывести ее на
# экран.
# Создать еще одну переменную равную среднему
# арифметическому возрасту, и вывести это значение
# на экран.
person_a = 49
person_b = 50
person_c = 23
all_person_summ = person_a + person_b + person_c
print('Сумма возрастов:', all_person_summ)
middle_age = all_person_summ // 3
print("Средний возраст:", middle_age)
