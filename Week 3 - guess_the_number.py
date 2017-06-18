# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
#                  
import simplegui
import random
import math

#initialize global variables used in your code
guess = 0
guess_count = 0
secret_number = 0
guess_range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guess_count
    guess_count = int(math.ceil(math.log(guess_range, 2)))
    
    secret_number = random.randrange(0,guess_range)
    
    print "New game started, guess a number from 0 to " + str(guess_range)
    print str(guess_count) + " guesses remaining. \n"

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global guess_range
    guess_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global guess_range
    guess_range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_count, guess_range

    print "You guessed " + guess
    guess_count -= 1

       
    if guess_count ==0:
        print "You are out of guesses! The secret number was " + str(secret_number)+"\n" 
        new_game()   
    
    elif int(guess) == secret_number:
        print "You are correct! \n"
        new_game()
            
            
    elif int(guess) < secret_number:
        print "Higher!"
        print "You have " + str(guess_count) + " guesses remaing.\n"
        
    else:
        print "Lower!"
        print "You have " + str(guess_count) + " guesses remaing.\n"       
            
    


    
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100]", range100, 200)
f.add_button("Range is [0,100]", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
f.start()

# always remember to check your completed program against the grading rubric
