array = [10, 5, 2, 6, 7, 8, 3, 9, 10]


def bubble_sort(my_list):
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list)-1-i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]


bubble_sort(array)

print(array)
