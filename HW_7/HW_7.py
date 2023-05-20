# 1.Вывод с помощью лямбды "Hello, name" (где 'name' это заданное имя)

greeting = lambda name: f"Hello, {name}"


# 2. Вывод с помощью лямбды "Hello, name" список имен в формате "Hello, name"


hello_for_everybody = lambda names_in_lam: [f"Hello, {name}" for name in names_in_lam]
second_greetings = hello_for_everybody()


# 3. Напишите 2-мя способами генератор который принимает список  numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# # и возвращает новый список только с положительными числами с обработкой исключений.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_arr = []


def get_list(list_numbers):
    try:
        for elem in list_numbers:
            if elem > 0:
                positive_arr.append(elem)
                yield elem
    except TypeError:
        print("no positive numbers")


all_positive = get_list(numbers)


# 4 Необходимо составить список чисел которые указывают на длину слов в строке: sentence = " thequick  brown fox jumps
# over the lazy dog", но только если слово не "the" с обработкой исключений


def length_of_sentence(sentence):
    for word in sentence.split(" "):
        try:
            if word != "the":
                yield len(word)
        except TypeError:
            pass
