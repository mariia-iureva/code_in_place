from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        go_from_bottom()
        move_to_next_column()
    if front_is_blocked():
        go_from_bottom()
def go_from_bottom():
    turn_left()
    while front_is_clear():
        check_and_put_beeper()
    if front_is_blocked():
        check_and_put_beeper()
        return_to_bottom()
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def check_and_put_beeper():
    if front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            move()
    if front_is_blocked():
        if no_beepers_present():
            put_beeper()
def move_to_next_column():
    move()
    move()
    move()
    move()
def return_to_bottom():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
