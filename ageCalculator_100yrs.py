"""
Character Input Exercise from http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Description:
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Pseudo-code:
1) Prompt the user for their name and store the value. No validation should be needed, names can be whatever.
2) Prompt the user for their age, in years. Check if the number is an int and repeat the question if not.
3) Calculate when the user will turn 100 years old
4) Tell the user when they should turn 100
"""

from datetime import date

def age_calc_100yrs():

    print 'Welcome to the age calculator app.'

    # Ask the user for their name
    usrname = raw_input('Hello! Please enter your name: ')

    # Ask the user for their age, in years
    while True:
        try:
            age = float(input('Please enter your age, in years: '))
        except:
            print 'Your age must be entered as a number. Please try again.'
            continue
        else:
            break

    yrs = 100 - int(age)
    hunyr = date.today().year + yrs

    if yrs > 0:
        print("Hi, %s! You'll be 100 years old in %s years, which will be %s." % (usrname, int(yrs), hunyr))
    elif yrs == 0:
        print("Congratulations %s! You're 100 years old! Keep it going!" % (usrname))
    else:
        print("Wow, %s! You turned 100 years old in %s, which was %s years ago. Awesome!" % (usrname, hunyr, abs(yrs)))

age_calc_100yrs()