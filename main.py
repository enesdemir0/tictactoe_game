num_list = [12, 16, 20, 23, 27, 31, 34, 38, 42]
list_x = []
list_o = []

winning_positions = [[12, 16, 20], [23, 27, 31], [34, 38, 42], [12, 23, 34], [16, 27, 38],
                     [20, 31, 42], [12, 27, 42], [20, 27, 34]]



def score(put_list, player_score=0):
    for winning_position in winning_positions:
        x = 0
        for num in winning_position:
            if num in put_list:
                x += 1
        if x == 3:
            player_score += 1
    return player_score


number_tuple = (12, 16, 20, 23, 27, 31, 34, 38, 42)


def game_board():
    for x in range(44):
        if x in [3, 7, 14, 18, 25, 29, 36, 40]:
            print("|", end='')
        elif x in [10, 21, 32, 43]:
            print("_")
        elif x in list_x:
            print("X", end="")
        elif x in list_o:
            print("O", end="")
        elif x in number_tuple:
            print(number_tuple.index(x) + 1, end="")
        else:
            print("_", end='')
    print("   |   |")


game_board()

for _ in range(4):
    move_x = int(input("Player 'X' which number you wanna put 'X': ")) - 1
    num_list.remove(number_tuple[move_x])
    list_x.append(number_tuple[move_x])
    game_board()

    move_y = int(input("Player 'O' which number you wanna put 'O': ")) - 1
    num_list.remove(number_tuple[move_y])
    list_o.append(number_tuple[move_y])
    game_board()


move_x = int(input("Player 'X' which number you wanna put 'X': ")) - 1
num_list.remove(number_tuple[move_x])
list_x.append(number_tuple[move_x])
game_board()


if score(list_x) == score(list_o):
    print("Draw")
elif score(list_x) > score(list_o):
    print("Congratulations player 'X' you won")
else:
    print("Congratulations player 'O' you won")
