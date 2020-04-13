"""Given a string that contains only digits from 0 to 9, and an integer value, target. Find out how many expressions
are possible which evaluate to target using binary operator +, – and * in given string of digits.

Input : "123",  Target : 6
Output : {“1+2+3”, “1*2*3”}

Input : “125”, Target : 7
Output : {“1*2+5”, “12-5”}
"""

numbers = list(map(int, input().split(' ')))
target = int(input())


def calculate_expressions(target_no, operator, numbers_list):
    pass
