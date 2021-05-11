"""
Prints out a randomly generated addition problem
and checks if the user answers correctly until the 
user has gotten 3 problems correct in a row.
"""

import random

NUMBER_OF_PROBLEMS_SOLVED = 3

def main():
    
    num1 = choose_number()
    num2 = choose_number()
    count = 1
    ai_result = solve_one_problem(num1, num2)
    human_result = ask_user(num1, num2)
    
    while count < NUMBER_OF_PROBLEMS_SOLVED:
        count = evaluate_human_result(ai_result, human_result, count)
        num1 = choose_number()
        num2 = choose_number()
        ai_result = solve_one_problem(num1, num2)
        human_result = ask_user(num1, num2)
        # count = evaluate_human_result(ai_result, human_result, count)
    print("Correct! You've gotten " + str(NUMBER_OF_PROBLEMS_SOLVED) + " correct in a row.")
    print("Congratulations! You mastered addition.")

def choose_number():
    random_number = random.randint(10,99)
    return random_number

def ask_user(num1, num2):
    print("What is " + str(num1) + " + " + str(num2) + "?")
    while True:
        try:
            human_result = int(input("Your answer: "))
            return human_result
        except ValueError:
            print('invalid choice')
    return human_result

def solve_one_problem(num1, num2):
    ai_result = num1 + num2
    return ai_result

def evaluate_human_result(ai_result, human_result, count):
    if ai_result == human_result:
        print("Correct! You've gotten " + str(count) + " correct in a row.")
        count += 1
    else:
        print("Incorrect. The expected answer is " + str(ai_result))
        count = 1
    return count
if __name__ == '__main__':
    main()
