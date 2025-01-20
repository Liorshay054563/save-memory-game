


def print_board(none_board):
    """ print the current board"""
    print(none_board[0:5])
    print(none_board[5:10])

def player_turn(board_one,none_board,playerT,player_a,player_b):
    """take card from user, check if same , update score"""
    try:
        while len(set(none_board)) != 1: # stop the func when no cards available

            pick1 = valid_input( board_one,none_board) # choose first card
            print(f"== {board_one[pick1]} ==")
            pick2 = valid_input( board_one,none_board) # choose second card
            print(f"== {board_one[pick2]} ==")
            if pick1 == pick2 or isinstance(pick1,str) or isinstance(pick2,str):
                print("Pick tow different cards")
                continue
            elif pick1 == 99 or pick2 == 99:
                print("RESTART game")
                break
            elif board_one[pick1] != board_one[pick2]:
                print(f"\n Wrong cards, next player turn\n")
            elif board_one[pick1] == board_one[pick2]: # if same
                print("Well play, go again")
                none_board[pick1] = "[]" # change the board
                none_board[pick2] = "[]"

                print_board(none_board) # print after changes
                # if same update score
                if playerT:
                    player_a += 1
                    player_b += 0
                else:
                    player_b += 1
                    player_a += 0

                player_a , player_b = player_turn(board_one, none_board, playerT, player_a, player_b) # if same pick cards again
                return player_a , player_b # return the score too 'main'


            return player_a, player_b # guessed wrong

        return player_a, player_b # stop the loop when no cards left
    except Exception as e:
        print(e)

def valid_input(board,none_board):
    """check if the pick is on board, or is free"""

    while True:
        try:
            pick = input("Choose your [card] in the board by pick a number: ")
            if pick == "R":
                print("restart game")
                exit()
            if int(pick) > len(board) or int(pick) < 0 or none_board[pick] == "[]" :
                print("your choose is not on board or not free, please choose again")

            else:
                return int(pick)
        # except ValueError as e:
        #     print(e)
        # except TypeError as e:
        #     print(e)
        except NameError as e:
            print(e)


def print_score(player_a,player_b,player_a_name,player_b_name):
    """ print the current board score"""
    print(f"player {player_a_name} = {player_a} ")
    print(f"player {player_b_name} = {player_b} ")




