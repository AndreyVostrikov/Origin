import SortBySelection


# Constant for switching debug and release mode
DEBUG_MODE = False

# Constant strings for debugging
DEBUG_MSG_INPUT_LIST = ["Input list: ", "Исходный список: "]
DEBUG_MSG_OUTPUT_LIST = ["Output list: ", "Отсортированный список: "]
LANGUAGE_OF_OUTPUT = ['Element not found', 'Элемент не найден']
INDEX_ELEMENT = ['index of element', 'Индекс элемента']
# Language selection
LANG_EN_CODE = 0
LANG_RU_CODE = 1


def binary_search(input_element, language = LANG_EN_CODE):
    element = input_element
    lst = SortBySelection.sort_by_selection([10, 234, 25, 52, 546])
    if DEBUG_MODE: print(DEBUG_MSG_OUTPUT_LIST[language], lst)
    left_border_list = 0
    right_border_list = len(lst)
    while left_border_list < right_border_list - 1:
        middle_list = (left_border_list + right_border_list) // 2
        if lst[middle_list] > element:
            right_border_list = middle_list
        else:
            left_border_list = middle_list
    if lst[left_border_list] == element:
        return print(INDEX_ELEMENT[language], left_border_list)
    elif lst[right_border_list] != element:
        return print(LANGUAGE_OF_OUTPUT[language])
    else:
        return print(INDEX_ELEMENT[language], right_border_list)


print(binary_search(522))