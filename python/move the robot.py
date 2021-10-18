#calling a function in a for loop
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def run():
    for i in range(1,7):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
run()

########OR############
#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
#def run():
#    move()
#    turn_left()
#    move()
#    turn_right()
#    move()
#    turn_right()
#    move()
#    turn_left()

#for i in range(1,7):
#    run()