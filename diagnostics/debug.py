"""
Part A:
The function divide_and_round() doesn't return anything back.
So the program will just print 10 instead of 5
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        new_n = n / 2 #creating new variable new_n to avoid confusion
    else:
        new_n = (n + 1) / 2
    return new_n #returning new_n back to the main function

def main():
    n = 10
    answer = divide_and_round(n) #creating new variable "answer" 
    # to get answer from the function divide_and_round(n) and store it
    print(answer) 
