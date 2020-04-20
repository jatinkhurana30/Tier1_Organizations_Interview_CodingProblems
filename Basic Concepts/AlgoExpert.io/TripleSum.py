"""Find a triplet that sum to a given value Given an array and a value, find if there is a triplet in array whose sum
is equal to the given value. If there is such a triplet present in array, then print the triplet and return true.
Else return false. For example, if the given array is {12, 3, 4, 1, 6, 9} and given sum is 24, then there is a
triplet (12, 3 and 9) present in array whose sum is 24 """

input_array = list(map(int, input().split(' ')))
triplet_sum = int(input())

triplet_pair = []


def remove_extra_pairs(double_pair_array):
    relevant_pairs = []
    for _ in double_pair_array:
        if not check_if_pair_exists(_, relevant_pairs):
            relevant_pairs.append(_)
    return relevant_pairs


def check_if_pair_exists(pair, remaining_pairs):
    flag = 0
    for remaining_pair in remaining_pairs:
        if pair == remaining_pair or (pair[0] == remaining_pair[1] and pair[1] == remaining_pair[0]):
            flag = 1
            break
    if flag == 1:
        return True
    else:
        return False


found = 0
for i in range(0, len(input_array)):
    pairing_array = input_array.copy()
    pairing_array.pop(i)
    double_pairs = [[j, k, j + k] for j in pairing_array for k in pairing_array if j != k]
    relevant_pair_array = remove_extra_pairs(double_pairs)
    for relevant_pair in relevant_pair_array:
        if triplet_sum - input_array[i] == relevant_pair[2]:
            triplet_pair.append(input_array[i])
            triplet_pair.append(relevant_pair[0])
            triplet_pair.append(relevant_pair[1])
            found = 1

    if found == 1:
        break

print(triplet_pair)
