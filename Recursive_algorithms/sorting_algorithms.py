list_one = [3, 1, 2, 4, 9]
list_two = [9, 9, 2, 3, 1, 6, 3, 6]
list_three = [9, 4, 9, 5, 5, 9, 1, 8]
passes = 0


def bubble_sort(list_to_sort):
    swapped = False
    global passes
    for i in range(0, len(list_to_sort) - 1):
        if list_to_sort[i] > list_to_sort[i + 1]:
            list_to_sort[i], list_to_sort[i + 1] = list_to_sort[i + 1], list_to_sort[i]
            swapped = True
            passes += 1
            bubble_sort(list_to_sort)
    if not swapped:
        print(list_to_sort)
        print(passes)

bubble_sort(list_three)
