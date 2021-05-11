"""
Prints out a randomly generated addition problem
and checks if the user answers correctly until the 
user has gotten 3 problems correct in a row.
"""

import random

NUMBER_OF_PROBLEMS_SOLVED = 3

def main():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    result = num1 + num2
    print("What is " + str(num1) + " + " + str(num2) + "?")
    result2 = int(input("Your answer: "))
    count = 1
    # for i in range(NUMBER_OF_PROBLEMS_SOLVED):
    while count < NUMBER_OF_PROBLEMS_SOLVED:
        if result == result2:
            print("Correct! You've gotten " + str(count) + " correct in a row.")
            count += 1
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            result = num1 + num2
            print("What is " + str(num1) + " + " + str(num2) + "?")
            result2 = int(input("Your answer: "))
        else:
            print("Incorrect. The expected answer is " + str(result))
            count = 1
            num1 = random.randint(10,99)
            num2 = random.randint(10,99)
            result = num1 + num2
            print("What is " + str(num1) + " + " + str(num2) + "?")
            result2 = int(input("Your answer: "))
    print("Correct! You've gotten " + str(NUMBER_OF_PROBLEMS_SOLVED) + " correct in a row.")
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()
