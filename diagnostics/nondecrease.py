def main():
    # TODO write your solution here
    welcome_message()
    count = play()
    exit_message(count)

def play()
    previous_number = float(input("Enter num: "))
    count = 1
    while True:
        next_number = float(input("Enter num: "))
    if next_number >= previous_number:
        count +=1
        previous_number = next_number
    else:
        return count
    
def welcome_message():
    print("Enter a sequence of non-decreasing numbers")
    
def exit_message(count)
    print("Thanks for playing!")
    print("Sequence length" + count)


if __name__ == "__main__":
    main()
