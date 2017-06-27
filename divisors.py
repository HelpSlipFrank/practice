"""
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

2017-06-27  Added a check if the number is prime
"""

def divisors():

    while True:
        try:
            val = int(input("Hey, man. Gimmie a number, and only a number. I'll give ya what its divisors are. Waddya say? "))
        except:
            print "Not cool dude. I said only numbers. Let's try this again, shall we. Now, do right this time."
            continue
        else:
            print "Thanks man. Lemme see what I got here."
            break

    div = [n for n in range(1, val+1) if val % n == 0]

    if len(div) == 2:
        print("'%d' is a prime number!" % val)
    else:
        print("'%d' has %d divisors, which are listed below:" % (val,len(div)))
        print div

divisors()