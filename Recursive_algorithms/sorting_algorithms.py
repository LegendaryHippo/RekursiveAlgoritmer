list_one = [9, 4, 9, 5, 5, 9, 1, 8, 4, 6, 3, 4, 1, 8, 5, 3, 44, 63, 31, 63, 11, 13, 64, 99, 11, 43, 25, 15, 32, 62, 74]
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
bubble_sort(list_one)
