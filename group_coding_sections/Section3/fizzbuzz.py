"""
Prints the Fizz Buzz sequence up to a given number.
"""
FIZZNUMBER = 3
BUZZNUMBER = 5
def main():
    numberOfTimes = input("How many times to run? ")
    numberOfTimesNumber = int(numberOfTimes)

    for number in range(numberOfTimesNumber):
        humanNumber = number + 1
        #modulo, remainder
        if (humanNumber % (FIZZNUMBER * BUZZNUMBER) == 0):
            print("fizzbuzz")
        elif humanNumber % FIZZNUMBER == 0:
            print("fizz")
        elif humanNumber % BUZZNUMBER == 0:
            print("buzz")
        else:
            print(str(humanNumber))
    # Fill this function out!
    pass
 
if __name__ == '__main__':
    main()
