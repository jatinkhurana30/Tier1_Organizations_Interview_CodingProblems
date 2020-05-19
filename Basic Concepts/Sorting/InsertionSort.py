array = [10, 5, 2, 6, 7, 8, 3, 9, 10]


def InsertionSort(my_array):
    for i in range(0, len(my_array)):
        for j in range(0, i):
            if my_array[j] > my_array[i]:
                my_array[j], my_array[i] = my_array[i], my_array[j]



InsertionSort(array)
print(array)


