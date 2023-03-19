
import pickle

#
#
# # 1. Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний и последний
# элементы данного файла. Если чисел меньше 3 выводить ошибку.


def output_from_file(file: str) -> str:
    """

    :rtype: object
    :param file: Имя файла с целыми числами
    :return: Вывод первого, второго, предпоследнего и последнего элементов
    """
    try:
        with open(file, "r") as f:
            string: str = f.readline()
            if len(string) < 3:
                return "Ошибка: в файле меньше 3-х чисел"
            else:
                return (
                    f"Вывод первого, второго, предпоследнего и "
                    f'последнего элементов файла "{file}": {string[0]}, '
                    f"{string[1]}, {string[-2]}, {string[-1]}"
                )
    except FileNotFoundError:
        print("Файл не найден")


#
#  2. Дан файл целых чисел. Создать два новых файла, первый из которых содержит четные числа из исходного файла,
#  а второй — нечетные (в том же порядке). Если четные или нечетные числа в исходном файле отсутствуют, то
# соответствующий результирующий файл оставить пустым.
#


def even_and_odd_numbers(file):
    """
    :param file: Имя файла с целыми числами
    :return: Два файла с четными и нечетными числами
    """
    even = []
    odd = []
    with open(file, "r") as f:
        sting: str = f.readline()
        for i in range(len(sting)):
            if int(sting[i]) % 2 == 0:
                even.append(sting[i])
            else:
                odd.append(sting[i])

        with open("even.txt", "w") as f1:
            if even:
                for i in even:
                    f1.write(i)

        with open("odd.txt", "w") as f2:
            if odd:
                for i in odd:
                    f2.write(i)

        with open("even.txt", "r") as f3:
            even = f3.readline()
        with open("odd.txt", "r") as f4:
            odd = f4.readline()

    return (
        f"Содержимое файла с четными числами: {even}\n"
        f"Содержимое файла с нечетными числами: {odd}"
    )


print(even_and_odd_numbers("file2.txt"))


# # 3.  Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.


def squares_of_real_numbers(file: str) -> str:
    """
    :param file: Имя файла с вещественными числами
    :return: Файл, с заменными элементами на их квадраты
    """

    with open(file, "r") as f:
        list_squares = [str(float(n) ** 2) for n in f.readline().split(" ")]

    with open(file, "w") as f:
        f.writelines(" ".join(list_squares))
        return f"Возведенные в квадрат вещественные числа: {list_squares}"


print(squares_of_real_numbers("file3.txt"))


# # 4.    Задание 4. Даны два файла произвольного типа. Поменять местами их содержимое.
# # Файлы должны быть бинарного типа


def swap_file_contents(file_1: str, str_1: str, file_2: str, str_2: str):
    """
    :param file_1: бинарный файл
    :param str_1: данные для записи во второй бинарный файл
    :param file_2: бинарный файл
    :param str_2: данный для записи в первый бинарный файл
    :return:
    """

    with open(file_1, "wb") as f1, open(file_2, "wb") as f2:
        pickle.dump(str_1, f1)
        pickle.dump(str_2, f2)

    with open(file_1, "rb") as f1, open(file_2, "rb") as f2:
        str_f1 = pickle.load(f1)
        str_f2 = pickle.load(f2)

    with open(file_1, "wb") as f1, open(file_2, "wb") as f2:
        pickle.dump(str_f2, f1)
        pickle.dump(str_f1, f2)

    with open(file_1, "rb") as f1, open(file_2, "rb") as f2:
        return (
            f"Содержимое первого файла: {pickle.load(f1)}\n"
            f"Содержимое второго файла: {pickle.load(f2)}"
        )


print(swap_file_contents("first.dat", "asdasda", "second.dat", "zxcxc"))
