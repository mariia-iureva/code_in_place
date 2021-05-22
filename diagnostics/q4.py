from karel.stanfordkarel import *

def main():
    # TODO write your solution here
    while front_is_clear():
        make_a_wave()
    

def make_a_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    get_back_to_the_first_street()
    if front_is_clear():
        make_gap()

def make_gap()
    move()
    move()
    
def get_back_to_the_first_street():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
