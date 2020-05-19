array = [10, 5, 2, 6, 7, 8, 3, 9, 10]


def SelectionSort(my_array):
    for i in range(0, len(my_array)):
        min_so_far = my_array[i]
        for j in range(i, len(my_array)):
            if my_array[j] < min_so_far:
                my_array[j], min_so_far = min_so_far, my_array[j]

        min_so_far, my_array[i] = my_array[i], min_so_far


SelectionSort(array)

print(array)