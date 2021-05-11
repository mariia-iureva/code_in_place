from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper on the middle of the first row.
"""

def main():
    """
    Your code here
    """
    if front_is_blocked():
        put_beeper()
    else:
        # put beepers in the corners
        put_beeper()
        while front_is_clear():
            move()
        put_beeper()
        turn_around()
        move()
        # return to first corner beeper
        while no_beepers_present():
            move()
        turn_around()
        move()
        while no_beepers_present():
            add_beeper_and_go_towards_another_corner()
        while front_is_clear():
            move()
            pick_beeper()
        turn_around()
        while no_beepers_present():
            move()
        
        while front_is_clear():
            move()
            pick_beeper()
        turn_around()
        while no_beepers_present():
            move()
    
def add_beeper_and_go_towards_another_corner():
    put_beeper()
    move()
    while no_beepers_present():
        move()
    turn_around()
    move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Midpoint8.w')
