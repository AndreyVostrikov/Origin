#                                        ЛИНЕЙНЫЙ ПОИСК
# Линейный поиск осуществляется из списка элементов введенных нами (количество элементов ограниченно 10-ю)
# Линейный поиск выводит индекс искомого нами элемента


def linear_search(number):
    lst = [int(input('1)Введите число:')), int(input('2)Введите число:')), int(input('3)Введите число:')),
           int(input('4)Введите число:')), int(input('5)Введите число:')), int(input('6)Введите число:')),
           int(input('7)Введите число:')), int(input('8)Введите число:')), int(input('9)Введите число:')),
           int(input('10)Введите число:'))]     # Ввод в список 10-ти значений
    index = 0
    x = len(lst) - 1
    while lst[index] != number and x > index:   # В данном циле проводится перебор каждого элемента по порядку
        index += 1
    if lst[index] == number:                    # Если элемент равен искомому - выводим его индекс
        return 'Индекс:', index
    else:                                       # В противном случае - выводим "Элемент не найден"
        return 'Элемент не найден'


print(linear_search(18))