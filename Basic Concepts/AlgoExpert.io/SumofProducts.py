"""
Input : A[] = {1, 3, 4}
Output : 19
Possible Pairs : (1,3), (1,4), (3,4)
Sum of Product : 1*3 + 1*4 + 3*4 = 19

"""

A = list(map(int, input().split(" ")))

pairs = [(a, b) for a in A for b in A if a != b]

relevant_pairs = []


def checkIf_exists(tuple, relevant_tuples):
    flag = 0
    for relevant_tuple in relevant_tuples:
        if tuple == relevant_tuple or (relevant_tuple[0] == tuple[1] and relevant_tuple[1] == tuple[0]):
            flag = 1
            break

    if flag == 1:
        return True
    else:
        return False


final_sum = 0
for pair in pairs:
    if not checkIf_exists(pair, relevant_pairs):
        relevant_pairs.append(pair)
        final_sum = final_sum + (pair[0] * pair[1])

print(final_sum)
print(relevant_pairs)
