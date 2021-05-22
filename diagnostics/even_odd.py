# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    # TODO write your solution here
    number = 1
    for number in range(MAX_NUMBER+1):
        if number % 2 == 0:
            print(number + " is even")
        else:
            print(number + " is odd")
        number += 1

if __name__ == "__main__":
    main()
