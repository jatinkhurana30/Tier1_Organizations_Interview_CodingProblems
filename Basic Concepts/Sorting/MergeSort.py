array = [10, 5, 2, 6, 7, 8, 3, 9, 10]


def merge_sort(input_array):
    if len(input_array) == 1:
        return input_array

    middle = len(input_array) // 2

    left_array = merge_sort(input_array[0:middle])
    right_array = merge_sort(input_array[middle: len(input_array)])
    answer = merge(left_array, right_array)
    return answer


def merge(left, right):
    i = j = 0
    final_array = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final_array.append(left[i])
            i += 1
        elif left[i] > right[j]:
            final_array.append(right[j])
            j += 1

    if i < len(left):
        while i < len(left):
            final_array.append(left[i])
            i += 1

    if j < len(right):
        while j < len(right):
            final_array.append(right[j])
            j += 1

    return final_array


merge_sort(array)
print(merge_sort(array))
print(array)
