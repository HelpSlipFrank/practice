"""
Odd or even exercise from http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Description:
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
    1) If the number is a multiple of 4, print out a different message.
    2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

def oddoreven():

    while True:

        while True:
            try:
                i = int(input('Please enter any integer (whole number): '))
            except:
                print "Hey, partner... Please enter an integer like a good boy/girl/thing. M'kay?"
                continue
            else:
                break

        if i % 2 == 0:
            print('Whoa there partner! That thar %s is one of the even numbers! Fancy...' % (i))
        elif i % 2 == 1:
            print('How about that. %s is an odd number, yes it is.' % (i))
        elif i % 4 == 0:
            print("Why did you enter %s!?! It's a fuckin' multiple of 4. You son of a bitch!" % (i))
        else:
            print 'What the fuck did you enter!?!'

        cont = raw_input('Do you want to continue? ')
        if cont.lower() == 'y' or cont.lower() == 'yes':
            continue
        elif cont.lower() == 'n' or cont.lower() == 'no':
            break
        else:
            print("I'm not sure what you meant by '%s', so I'm gonna assume you're tired and quit this thing." % (cont))
            break


oddoreven()