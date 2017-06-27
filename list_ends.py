"""
http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
first and last elements of the given list. For practice, write this code inside a function.
"""

import random as ran

def list_ends():
    # Generate a random list of ints. The length is also random, but it will be between 10 and 25 ints long.
    lst0 = [ran.randint(0,100) for n in range(ran.randint(10,25))]
    print "Here's your list:\n" + str(lst0)

    # From the first list, create a new list consisting of the first and last elements
    lst1 = [lst0[0], lst0[len(lst0)-1]]
    print "Here's the new list:\n" + str(lst1)

list_ends()
