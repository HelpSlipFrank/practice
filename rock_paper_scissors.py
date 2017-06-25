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
        input = [raw_input("Press your keys now!")]


def welcome():
    print """
    Welcome to RPS in python!
    To play, each player takes control of their input keys. This is best played on a keyboard with a 10-digit keypad.
    Player 1 will use keys a, s, d to control their throw:
        a = Rock
        b = Paper
        c = Scissors
        
    Player 2 will use keys 1, 2, 3 to control their throw:
        1 = Rock
        2 = Paper
        3 = Scissors
        
    When the game tells you, simultaneously press your keys to throw!
    Ready?
    \n
    """

welcome()