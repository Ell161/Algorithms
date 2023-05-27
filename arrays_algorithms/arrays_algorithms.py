from typing import List


def sort_bubble(numbers_list: list) -> List:
    print('\n*Сортировка пузырьком*')
    for current_index in range(len(numbers_list) - 1):
        is_sorted = True
        for i in range(len(numbers_list) - 1 - current_index):
            if numbers_list[i] > numbers_list[i + 1]:
                is_sorted = False
                numbers_list[i], numbers_list[i + 1] = numbers_list[i + 1], numbers_list[i]
        if is_sorted:
            break
    return numbers_list


def selection_sort(numbers_list: list) -> List:
    print('\n*Сортировка выбором*')
    for current_index in range(len(numbers_list) - 1):
        min_element = current_index
        for i in range(current_index + 1, len(numbers_list)):
            if numbers_list[i] < numbers_list[min_element]:
                min_element = i
        if min_element != current_index:
            numbers_list[current_index], numbers_list[min_element] = numbers_list[min_element], numbers_list[
                current_index]
    return numbers_list


def binary_search_recursive(numbers_list, find_number, start_index, end_index) -> int:
    if end_index >= start_index:
        middle = (start_index + end_index) // 2
        if numbers_list[middle] == find_number:
            return middle
        elif numbers_list[middle] > find_number:
            return binary_search_recursive(numbers_list, find_number, start_index, middle - 1)
        else:
            return binary_search_recursive(numbers_list, find_number, middle + 1, end_index)
    else:
        return -1


# Homework

my_list = [1, 2, 3, 3, 2, 3, 4, 2, 1, 1, 2, 3, 4, 4, 2, 3, 1, 4, 2, 3, 4, 2, 1, 2, 3, 4, 2, 1, 3, 4, 2, 1, 2, 3, 4, 4,
           2, 3, 3, 2, 4]


def counting_sort(numbers_list: list) -> List:
    print('\n*Сортировка подсчетом*')
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    count_list = [0 for _ in range(max_value - min_value + 1)]
    for element in numbers_list:
        count_list[element - min_value] += 1

    index = 0
    for i in range(len(count_list)):
        for element in range(count_list[i]):
            numbers_list[index] = i + min_value
            index += 1
    return numbers_list


sort_list = counting_sort(my_list)
print(sort_list)
