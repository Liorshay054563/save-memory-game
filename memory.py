# Memory Game
import random

from memory_func import *

board_one =['a','b','c','d','e','a','b','c','d','e'] # the real cards
#random.shuffle(board_one)

none_board = [f"[{i}]" for i in range(len(board_one))] # same cards but none, cards by number for user pick

player_a_name = input("Enter first player: ") # input player A name
player_b_name = input("Enter second player: ") # input player A name
player_a = 0 # player A score
player_b = 0 # player B score
pick = None # the player choice
playerT = True # change the player turn

while any(card != "[]" for card in none_board): # stop when all cards are "[]", no cards left
    try:

        print_score(player_a, player_b, player_a_name, player_b_name)
        print_board(none_board) # print the board

        print(f"\n=== {player_a_name if playerT else player_b_name}'s turn ===")
        # run func player_turn, and catch the score from the func
        player_a, player_b = player_turn(board_one, none_board, playerT,player_a,player_b)
        #print_score(player_a, player_b, player_a_name, player_b_name)

        playerT = not playerT # change turn to player B


    except TypeError as e:
        print(e)
print_score(player_a, player_b, player_a_name, player_b_name)
print(f"\n=== {player_a_name if player_a > player_b else player_b_name} You are the Winner!! ===")





#input 2 players name
# show them the unsolve board card
# player 'a' turn , pick up card and show it
# player 'a' turn , pick up  a second card and show it
# if cards same ,add 1 to score player, give another turn, remove the card from board
# now same player "b"....
# finish when no cards left on board
# count who's player score more