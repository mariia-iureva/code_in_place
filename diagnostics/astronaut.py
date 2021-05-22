def main():
    """asks the user for their height in meters and prints whether 
    or not they are the correct height to be a NASA astronaut."""
    user_height = input_height()
    check_height(user_height)

"""function returns user_height as an input from user. 
Only valid numbers are allowed. Otherwise promting for input repeats"""
def input_height():
    user_height = float(input("Enter your height in meters: "))
    
""" Here's option, when we need to validate user's input
    user_height = 0
    while user_height == 0:
        try:
            user_height = float(input("Enter your height in meters: "))
        except ValueError:
            user_height = 0 
"""
    return user_height

"""function checks if user can be an astronaut"""
def check_height(user_height):
    if user_height >= 1.6 and user_height <= 1.9:
        print("Correct height to be an astronaut")
    elif user_height < 1.6:
        print("Below minimum astronaut height")
    else:
        print("Above maximum astronaut height")



if __name__ == "__main__:
    main()
