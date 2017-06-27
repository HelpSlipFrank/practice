"""
http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    Keep the game going until the user types "exit"
    Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

def guessing_game():
    print "I'll give you a number between 1 and 9. You try to guess it. Ready?"

    while True:
        ran = random.randint(1,9)
        count = 0
        print "\nOK, I've got a number..."

        while True:
            guess = int(input("What's your guess? "))
            if guess ==  ran:
                print "Correct! You guessed the number!"
                count += 1
                break
            elif guess > ran:
                print "Lower... Try again."
                count += 1
                continue
            else:
                print "Higher... Try again"
                count += 1
                continue

        if count == 1:
            print "Damn, you got it on the first try! Good job"
        else:
            print("It took %d guesses to find the number." % count)

        cont = raw_input("Do you want to play again? ")

        if cont.lower() == 'y' or cont.lower() == 'yes' or cont.lower() == '':
            continue
        else:
            print "Thanks for playing! Goodbye!"
            break

guessing_game()
