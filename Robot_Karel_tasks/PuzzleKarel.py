from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
program to make Karel put last piece of puzzle and return back. 
We're using some new functions here (move_twice(), turn_right(),
pick_last_piece(), put_puzzle(), return_karel()
    """
    
    pick_last_piece()
    put_puzzle()
    return_karel()
def move_twice():
    move()
    move()
def pick_last_piece():
    move_twice()
    pick_beeper()

def put_puzzle():
    move()
    turn_left()
    move_twice()
    put_beeper()
def return_karel():
    turn_left()
    turn_left()
    move_twice()
    turn_right()
    move_twice()
    move()
    turn_left()
    turn_left() 
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        



if __name__ == '__main__':
    run_karel_program('Puzzle.w')
