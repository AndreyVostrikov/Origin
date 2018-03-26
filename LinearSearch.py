#                                        ЛИНЕЙНЫЙ ПОИСК
# Линейный поиск осуществляется из списка элементов введенных нами (количество элементов ограниченно 10-ю)
# Линейный поиск выводит индекс искомого нами элемента

from random import randint
A = int(input('Enter size of the list:'))
random_list = []
i = 0
while i < A:
    random_list.append(randint(1, 100))
    i += 1
print(random_list)
number_of_search = int(input('Enter number of search:'))




def linear_search(lst, number):
    index = 0
    x = len(lst) - 1
    while lst[index] != number and x > index:   # В данном циле проводится перебор каждого элемента по порядку
        index += 1
    if lst[index] == number:                    # Если элемент равен искомому - выводим его индекс
        return 'Индекс:', index
    else:                                       # В противном случае - выводим "Элемент не найден"
        return 'Элемент не найден'


print(linear_search(random_list, number_of_search))