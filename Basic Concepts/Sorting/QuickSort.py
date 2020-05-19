array = [10, 5, 2, 6, 7, 8, 3, 9, 10]


def QuickSort(input_array):
    pivot_index = len(input_array) - 1
    i = 0
    if len(input_array) <= 1:
        return
    while i < pivot_index:
        if input_array[i] >= input_array[pivot_index]:
            input_array[pivot_index], input_array[pivot_index - 1] = input_array[pivot_index - 1], input_array[
                pivot_index]
            if i != pivot_index - 1:
                input_array[i], input_array[pivot_index] = input_array[pivot_index], input_array[i]

            pivot_index -= 1
            i -= 1
        i += 1

    QuickSort(input_array[0: pivot_index])
    QuickSort(input_array[pivot_index:len(input_array)])


QuickSort(array)
print(array)
