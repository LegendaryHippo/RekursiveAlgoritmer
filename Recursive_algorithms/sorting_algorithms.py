list_one = [3, 1, 2, 4, 9]
list_two = [9, 9, 2, 3, 1, 6, 3, 6]


def bubble_sort(list_to_sort):
    swapped = False
    for i in range(0, len(list_to_sort) - 1):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            swapped = True
            bubble_sort(list_to_sort)
    if not swapped:
        print(list_to_sort)

bubble_sort(list_two)
