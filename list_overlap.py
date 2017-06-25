"""
http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without
duplicates). Make sure your program works on two lists of different sizes.

Extras:

    Randomly generate two lists to test this
    Write this in one line of Python (don't worry if you can't figure this out at this point - we'll get to it soon)

Lessons Learned:
1) randint(low, high) and randrange(low, high, step_frequency) can be used for random number generation
2) set(set_01).intersection(set_02) will convert both lists to sets and then output commonalities
"""

import random

def list_overlap():

    rand0 = [random.randint(0, 100) for r in xrange(20)]
    rand1 = [random.randint(0, 100) for r in xrange(25)]

    fin = set(rand0).intersection(rand1)
    print rand0
    print rand1
    print fin

list_overlap()