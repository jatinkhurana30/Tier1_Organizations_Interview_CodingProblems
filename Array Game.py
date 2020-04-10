"""Let's play a game on an array! You're standing at index 0 of an n-element array named game. From some index i
you can perform one of the following moves:

Move Backward: If cell i-1 exists and contains 0 , you can walk back to cell i-1 . Move Forward: If cell i+1 contains
a zero, you can walk to cell i+1 . If cell 9=i+leap  contains a zero, you can jump to cell i+leap . If you're
standing in cell n-1  or the value of n>i+leap, you can walk or jump off the end of the array and win the game. In
other words, you can move from index i  to index i+1 ,i-1 , or i+leap  as long as the destination index is a cell
containing 0 . If the destination index is greater than n-1, you win the game.

Given leap and game array, complete the function in the editor below so that it returns true if you can win the game
(or false if you cannot).

Sample Input:

5
0 0 0 1 1 1
Output : YES

Input 2:
3
0 0 1 1 1 0

Output:
NO

"""

leap = int(input())
game = list(map(int, input().split(' ')))


def can_win_game(game_array, leap_value, current_position):
    if current_position > len(game) - 1 or game_array[current_position] == 0:
        return True

    if game_array[current_position] == 0:
        game_array[current_position] = 2

    return (can_win_game(game_array, leap_value, current_position - 1) or
            can_win_game(game_array, leap_value, current_position + 1) or
            can_win_game(game_array, leap_value, current_position + leap)
            )


if can_win_game(game, leap, 0):
    print('YES')
else:
    print('NO')
