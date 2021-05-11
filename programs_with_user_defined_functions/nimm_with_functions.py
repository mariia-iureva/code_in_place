"""
TODO: Write a description here

There are 1 stones left
Player 2 would you like to remove 1 or 2 stones? 1

Player 1 wins!
"""
# python nimm.py

import random
THE_PILE = 20
def main():
    new_pile = THE_PILE
    who_was_the_last_to_play = play_nimm(new_pile)
    # print(who_was_the_last_to_play)
    winner = determine_winner(who_was_the_last_to_play)

def play_nimm(new_pile):
    while new_pile > 0:
        for i in range(2):
            whose_turn = i+1
            # adding an if to stop the for loop in the middle if there're no stones
            if new_pile == 0:
                return whose_turn
            elif new_pile == 1:
                print("There is " + str(new_pile) + " stone left")
                try:
                    choice = int(input("Player " + str(whose_turn) + ", you can only enter 1 now: "))
                # if user input is blank, we say, user entered 0, else we convert input into int
                except ValueError:
                    choice = 0
                while choice > 1 or choice <= 0:
                    try:
                        choice = int(input("Please enter 1: "))
                    # is user input is blank, we say, user entered 0
                    except ValueError:
                            choice = 0
                return whose_turn
            elif new_pile == 2:
                print("There are " + str(new_pile) + " stones left")
            # dealing with user input for stones
                try:
                    choice = int(input("Player " + str(whose_turn) + " would you like to remove 1 or 2 stones? "))
                # is user input is blank or letters, we say, user entered 0, else we convert input into int
                except ValueError:
                    choice = 0
                # validating input - only 1 or 2 is allowed
                while choice > 2 or choice <= 0:
                    try:
                        choice = int(input("Please enter 1 or 2: "))
                # is user input is blank, we say, user entered 0
                    except ValueError:
                        choice = 0
                if choice == 2:
                    return whose_turn
            else:
                print("There are " + str(new_pile) + " stones left")
            # dealing with user input for stones
                try:
                    choice = int(input("Player " + str(whose_turn) + " would you like to remove 1 or 2 stones? "))
                # is user input is blank or letters, we say, user entered 0, else we convert input into int
                except ValueError:
                    choice = 0
                # validating input - only 1 or 2 is allowed
                while choice > 2 or choice <= 0:
                    try:
                        choice = int(input("Please enter 1 or 2: "))
                # is user input is blank, we say, user entered 0
                    except ValueError:
                        choice = 0
                
            print("")
            new_pile -= choice
    return whose_turn
                
    # define a winner
    # print(whose_turn)
def determine_winner(whose_turn):
    if whose_turn == 1:
        winner = 2
    else:
        winner = 1
    # return winner
    print("")
    print("Player " + str(winner) + " wins!")

if __name__ == '__main__':
    main()
