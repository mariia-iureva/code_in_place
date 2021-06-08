"""
Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

def main():
    total = 0
    maximumInputNumber = 0
    minimumInputNumber = 100
    userInputNumber = 1

    while userInputNumber != 0:
        # string

        userInput = input("Enter a value: ")
        userInputNumber = int(userInput)
        # total = total + userInputNumber
        total += userInputNumber
        if userInputNumber > maximumInputNumber:
            maximumInputNumber = userInputNumber
        if userInputNumber < minimumInputNumber:
            minimumInputNumber = userInputNumber
            
        print("Running total is " + str(total))
        print("Minimum Value " + str(minimumInputNumber))
        print("Maximum Value " + str(maximumInputNumber))
if __name__ == '__main__':
    main()
