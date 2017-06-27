"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock

"""

def rock_paper_scissors():
    while True:
        throws = [char for char in raw_input("P1 and P2, press your keys now and then press 'Enter' to commit!")]

        # Store player throws
        p1 = [n for n in throws if (n.lower() == 'a' or n.lower() == 's' or n.lower() == 'd')]
        p2 = [n for n in throws if (n == '1' or n == '2' or n == '3')]

        # Check if both players properly provided a response
        if len(p1) < 1 or len(p2) < 1:
            if len(p1) < 1 and len(p2) >= 1:
                # If P1 didn't give a response and P2 did
                print "Round will restart since Player 1 didn't give a correct response."
                continue
            elif len(p2) < 1 and len(p1) >= 1:
                # If P2 didn't give a response and P1 did
                print "Round will restart since Player 2 didn't give a correct response."
                continue
            else:
                # Neither player gave a response
                print "Round will restart since both players didn't give a correct response."
                continue

        who_won(p1, p2)

        #Repeat?
        play_again = raw_input("\nDo you want to play again? (y/n) ")
        if play_again.lower() == 'y' or play_again.lower() == 'yes':
            continue
        elif play_again.lower() == 'n' or play_again.lower() == 'no':
            break
        else:
            break


def who_won(p1, p2):

    p1 = str(p1[0])
    p2 = str(p2[0])

    # Check for ties
    if (p1 == 'a' and p2 == '1') or (p1 == 's' and p2 == '2') or (p1 == 'd' and p2 == '3'):
        print "Tie!"
        print "No winner!"
    # Rock beats scissors
    elif (p1 == 'a' or p2 == '1') and (p1 == 's' or p2 == '2'):
        print 'Rock beats scissors!'
        if p1 == 'a':
            print 'Player 1 wins!'
        else:
            print 'Player 2 wins!'
    # Scissors beats paper
    elif (p1 == 's' or p2 == '2') and (p1 == 'd' or p2 == '3'):
        print 'Scissors beats paper!'
        if p1 == 's':
            print 'Player 1 wins!'
        else:
            print 'Player 2 wins!'
    # Paper beats rock
    elif (p1 == 'd' or p2 == '3') and (p1 == 'a' or p2 == '1'):
        print 'Paper beats rock!'
        if p1 == 'd':
            print 'Player 1 wins!'
        else:
            print 'Player 2 wins!'


def welcome():
    print """
    Welcome to RPS in python!
    To play, each player takes control of their input keys. This is best played on a keyboard with a 10-digit keypad.
    Player 1 will use keys a, s, d to control their throw:
        a = Rock
        s = Scissors
        d = Paper
        
    Player 2 will use keys 1, 2, 3 to control their throw:
        1 = Rock
        2 = Scissors
        3 = Paper
        
    When the game tells you, simultaneously press your keys to throw!
    But, don't spam the keyboard. Only press your key once.
    Ready?
    \n
    """

    rock_paper_scissors()

welcome()