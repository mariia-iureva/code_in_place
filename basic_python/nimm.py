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
    while new_pile > 0:
        for i in range(2):
            whose_turn = i
            # adding a break to stop the if in the middle if there're no stones
            if new_pile == 0:
                whose_turn = 0
                break
            print("There are " + str(new_pile) + " stones left")
            # dealing with user input for stones
            choice_input = input("Player " + str(i+1) + " would you like to remove 1 or 2 stones? ")
            # is user input is blank, we say, user entered 0, else we convert input into int
            if choice_input == '':
                choice = 0
            else:
                choice = int(choice_input)
            # validating input - only 1 or 2 is allowed
            while choice > 2 or choice <= 0:
                choice_input = input("Please enter 1 or 2: ")
            # is user input is blank, we say, user entered 0, else we convert input into int
                if choice_input == '':
                    choice = 0
                else:
                    choice = int(choice_input)
            # validating last step input. if there's only 1 stone left, user have to input 1
            while choice > new_pile:
                choice_input = input("You can only enter " + str(new_pile) + " now: ")
                # is user input is blank, we say, user entered 0, else we convert input into int
                if choice_input == '':
                    choice = 0
                else:
                    choice = int(choice_input)
            print("")
            new_pile -= choice
                
    # define a winner
    # print(whose_turn)
    if whose_turn == 0:
        winner = 2
    else:
        winner = 1
    
    print("Player " + str(winner) + " wins!")

if __name__ == '__main__':
    main()
