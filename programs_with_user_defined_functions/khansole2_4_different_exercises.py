"""
Asks user what type of a math excersize they wanna practice
Prints out a randomly generated math problem
and checks if the user answers correctly.
"""

import random 

NUMBER_OF_PROBLEMS_SOLVED = 3

def main():


    # num3 = random.randint(1,9)
    
    # substruction_result = add1 - add2
    # multiplication_result = add1 * num3
    # division_result = add1

    # we are gving the user 4 options to choose from:

    new_lesson = 1
    while new_lesson == 1:
        lesson_type = choose_lesson()
        lesson = study(lesson_type)
        new_lesson = practice_more()
    say_goodbye()

def study(lesson_type):
        if lesson_type == 1: #addition
            practice_addition()
        if lesson_type == 2: #subtraction
            practice_subtraction()
        if lesson_type == 3: #multiplication
            practice_multiplication()
        if lesson_type == 4: #division
            practice_division()
        
        
def choose_lesson():
    print("What would you like to practice? Choose:")
    print(" 1 for addition \n 2 for subtraction \n 3 for multiplication \n 4 for division")
    # we're checking if user input is valid and if what they entered is not text, not blank, not greater than 4
    try:
        lesson_type = int(input("Choose 1, 2, 3 or 4 to start the practice:"))
    except ValueError:
        lesson_type = 0
    # validating input - only 1,2,3,4 is allowed
    while lesson_type > 4 or lesson_type <= 0:
        try:
            lesson_type = int(input("Only numbers 1,2,3 or 4 would work, please, try again: "))
        except ValueError:
            lesson_type = 0
    return lesson_type
        
def practice_addition():
    print("Addition")
    num1 = choose_number()
    num2 = choose_number()
    lesson_type = 1
    count = 1
    ai_result = ai_solves_problem(num1, num2, lesson_type)
    human_result = user_solves_problem(num1, num2, lesson_type)
    
    while count <= NUMBER_OF_PROBLEMS_SOLVED:
        if count == NUMBER_OF_PROBLEMS_SOLVED:
            break
        else:
            count = evaluate_human_result(ai_result, human_result, count)
            num1 = choose_number()
            num2 = choose_number()
            ai_result = ai_solves_problem(num1, num2, lesson_type)
            human_result = user_solves_problem(num1, num2, lesson_type)
        # count = evaluate_human_result(ai_result, human_result, count)
    print("Correct! You've gotten " + str(NUMBER_OF_PROBLEMS_SOLVED) + " correct in a row.")
    print("Congratulations! You mastered addition.")

def choose_number():
    random_number = random.randint(10,99)
    return random_number

def choose_small_number():
    random_number = random.randint(1,9)
    return random_number

def user_solves_problem(num1, num2, lesson_type):
    if lesson_type == 1:
        print("What is " + str(num1) + " + " + str(num2) + "?")
    if lesson_type == 2:
        print("What is " + str(num1) + " - " + str(num2) + "?")
    if lesson_type == 3:
        print("What is " + str(num1) + " * " + str(num2) + "?")
    if lesson_type == 4:
        print("What is " + str(num1 * num2) + " / " + str(num2) + "?")
    
    while True:
        try:
            human_result = int(input("Your answer: "))
            return human_result
        except ValueError:
            print('invalid input')
    return human_result

def ai_solves_problem(num1, num2, lesson_type):
    if lesson_type == 1:
        ai_result = num1 + num2
    if lesson_type == 2:
        ai_result = num1 - num2
    if lesson_type == 3:
        ai_result = num1 * num2
    if lesson_type == 4:
        ai_result = (num1 * num2) / num2
    return ai_result

def evaluate_human_result(ai_result, human_result, count):
    if ai_result == human_result:
        print("Correct! You've gotten " + str(count) + " correct in a row.")
        count += 1
    else:
        print("Incorrect. The expected answer is " + str(ai_result))
        count = 1
    return count
            
def practice_subtraction():
    print("Subtraction")
    num1 = choose_number()
    num2 = choose_number()
    count = 1
    lesson_type = 2
    ai_result = ai_solves_problem(num1, num2, lesson_type)
    human_result = user_solves_problem(num1, num2, lesson_type)
    
    while count <= NUMBER_OF_PROBLEMS_SOLVED:
        if count == NUMBER_OF_PROBLEMS_SOLVED:
            break
        else:
            count = evaluate_human_result(ai_result, human_result, count)
            num1 = choose_number()
            num2 = choose_number()
            ai_result = ai_solves_problem(num1, num2, lesson_type)
            human_result = user_solves_problem(num1, num2, lesson_type)
        # count = evaluate_human_result(ai_result, human_result, count)
    print("Correct! You've gotten " + str(NUMBER_OF_PROBLEMS_SOLVED) + " correct in a row.")
    print("Congratulations! You mastered addition.")

def practice_multiplication(): #multiplication
    print("Multiplication")
    num1 = choose_number()
    num2 = choose_small_number()
    lesson_type = 3
    count = 1
    ai_result = ai_solves_problem(num1, num2, lesson_type)
    human_result = user_solves_problem(num1, num2, lesson_type)
    
    while count <= NUMBER_OF_PROBLEMS_SOLVED:
        if count == NUMBER_OF_PROBLEMS_SOLVED:
            break
        else:
            count = evaluate_human_result(ai_result, human_result, count)
            num1 = choose_number()
            num2 = choose_small_number()
            ai_result = ai_solves_problem(num1, num2, lesson_type)
            human_result = user_solves_problem(num1, num2, lesson_type)
        # count = evaluate_human_result(ai_result, human_result, count)
    print("Correct! You've gotten " + str(NUMBER_OF_PROBLEMS_SOLVED) + " correct in a row.")
    print("Congratulations! You mastered multiplication.")

def practice_division(): #division
    print("Division")

    num1 = choose_number()
    num2 = choose_small_number()
    lesson_type = 4
    count = 1
    ai_result = ai_solves_problem(num1, num2, lesson_type)
    human_result = user_solves_problem(num1, num2, lesson_type)
    
    while count <= NUMBER_OF_PROBLEMS_SOLVED:
        if count == NUMBER_OF_PROBLEMS_SOLVED:
            break
        else:
            count = evaluate_human_result(ai_result, human_result, count)
            num1 = choose_number()
            num2 = choose_small_number()
            ai_result = ai_solves_problem(num1, num2, lesson_type)
            human_result = user_solves_problem(num1, num2, lesson_type)
        # count = evaluate_human_result(ai_result, human_result, count)
    print("Correct! You've gotten " + str(NUMBER_OF_PROBLEMS_SOLVED) + " correct in a row.")
    print("Congratulations! You mastered division.")

def practice_more():
    new_lesson_input = input("Would you like to play again? Type yes or no:")
    if new_lesson_input == "no":
        new_lesson = 0
    elif new_lesson_input == "yes":
        new_lesson = 1
    else:
        print("We take it as a \"yes\" :)")
        new_lesson = 1
    return new_lesson

def say_goodbye():
    print("Hope, you enjoyed it. Have a wonderful day!")

if __name__ == '__main__':
    main()
