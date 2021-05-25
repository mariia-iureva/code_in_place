"""
Simulates a magic eight ball.
Prompts the user to type a yes or no question and gives
a random answer from a set of prefabricated responses.
"""
import random

# make a bunch of random answers
ANSWER_1 = "Ask again later."
ANSWER_2 = "No way."
ANSWER_3 = "Without a doubt."
ANSWER_4 = "Yes."
ANSWER_5 = "Possibly."
def main():
    # Fill this function out!
    number = random.randint(1,5)
# ask the user
    # name: question, type: string
    question = input("Ask a yes or no question: ")

    # is question (string) the same as 0 (number)
    while question != "":
        # pick a random answer and tell the user the answer
        if number == 1:
            print(ANSWER_1)
        if number == 2:
            print(ANSWER_2)
        if number == 3:
            print(ANSWER_3)
        if number == 4:
            print(ANSWER_4)
        if number == 5:
            print(ANSWER_5)
        question = input("Ask a yes or no question: ")
    

if __name__ == "__main__":
    main()
