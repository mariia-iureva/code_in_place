from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    # moving up
    for i in range(19):
        move()
    # drawing 1 line
    turn_right()
    for i in range(11):
        move()
    for i in range(8):
        paint()
    get_back()
    # 2 line
    for i in range(10):
        move()
    for i in range(10):
        paint_corner(RED)
        if front_is_clear():
            move()
    get_back()
    # line 3
    for i in range(10):
        move()
    for i in range(2):
        paint()
    # this is an eye
    move()
    for i in range(7):
        paint_corner(RED)
        if front_is_clear():
            move()
    get_back()
    # line 4-6
    for i in range(3):
        for i in range(10):
            move()
        for i in range(10):
            paint_corner(RED)
            if front_is_clear():
                move()
        get_back()
    # line 7
    for i in range(10):
        move()
    for i in range(5):
        paint()
    get_back()
    # line 8
    for i in range(10):
        move()
    for i in range(8):
        paint()
    get_back()
    # line 9
    paint()
    for i in range(8):
        move()
    for i in range(5):
        paint()
    get_back()
    # line 10
    paint()
    for i in range(7):
        move()
    for i in range(6):
        paint()
    get_back()
    # line 11
    for i in range(2):
        paint()
    for i in range(4):
        move()
    for i in range(10):
        paint()
    get_back()
    # line 12
    for i in range(3):
        paint()
    for i in range(2):
        move()
    for i in range(9):
        paint()
    move()
    paint_corner(RED)
    get_back()
    # line 13
    for i in range(14):
        paint()
    get_back()
    # line 14
    move()
    for i in range(13):
        paint()
    get_back()
    # line 15
    move()
    move()
    for i in range(11):
        paint()
    get_back()
    # line 16
    for i in range(3):
        move()
    for i in range(10):
        paint()
    get_back()
    # line 17
    for i in range(4):
        move()
    for i in range(4):
        paint()
    move()
    for i in range(3):
        paint()
    get_back()
    # line 18
    for i in range(5):
        move()
    for i in range(2):
        paint()
    move()
    move()
    move()
    paint()
    get_back()
    # line 19
    for i in range(5):
        move()
    paint()
    for i in range(4):
        move()
    paint()
    get_back()
    # finally last one! 20th
    for i in range(5):
        move()
    paint()
    paint()
    for i in range(3):
        move()
    paint()
    paint()
    get_back()    
def get_back():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    move()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def paint():
    paint_corner(RED)
    move()

    


if __name__ == "__main__":
    run_karel_program()
