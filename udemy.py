# Homework assignments for the Udemy course
import math
import string


def sphere_vol(rad):
    """
    Description: Computes the volume of a sphere, given it's radius. The equation is:
        V=(4/3)*pi*r^3
    INPUT: rad = Radius of the sphere
    RETURN: The volume of the sphere
    """
    vol = (4/3)*math.pi*rad**3
    return vol


def range_check(low, high, num):
    """
    Description: Determine if a given number is within a range of numbers
    :param low: The low number in the range
    :param high: The high number in the range
    :param num: The number to determine if it is within the range
    :return: Returns a bool
    """

    # We need to create a range() and then for each item in the range, see if it matches the input number
    range_list = range(low, high)
    print range_list
    for val in range_list:
        print 'Checking ' + str(num) + ' against the range value ' + str(val)
        if num == val:
            found = True
            break
        else:
            found = False
            continue

    if found == True:
        return 'Yes, the number ' + str(num) + ' was found in the range ' + str(low) + ' to ' + str(high)
    else:
        return 'No, the number ' + str(num) + ' was NOT found in the range ' + str(low) + ' to ' + str(high)


def case_count(in_str):
    """
    Description: Takes in a string and calculates the number of upper and lower case characters within the string
    :param in_str:
    :return: Nothing returned. Will print directly to the screen
    """

    upper = 0
    lower = 0

    # Write all characters in the string to a list
    chars = [letter for letter in in_str if letter.isalpha() == True]

    # For every character in the list, check if it is uppercase or lowercase.
    for l in chars:
        if l.isupper():
            upper += 1
        else:
            lower += 1

    print 'Upper-case characters = ' + str(upper)
    print 'Lower-case characters = ' + str(lower)


def unique_list(in_lst):
    """
    Description: Take in a list and return a new list of all unique items from the list
    :param in_lst: Input list, containing integers
    :return: A list containing only unique values
    """
    # Will will do this by casting the list to a new set
    print set(in_lst)


def multiply(num_list):
    """
    Description: Multiplies all elements in a list
    :param num: Input is a list of integers
    :return: Nothing. Directly prints the answer
    """

    total = 1

    for number in num_list:
        total = total * number

    print 'The total of all numbers in the list, multiplied together, is ' + str(total)


def palindrome(in_str):
    """
    :description: Takes in a string and determines if it is a palindrome
    :param string: Input string
    :return: If the given string is a palindrome
    """

    # Reverse the input string
    reverse_str = in_str[::-1]
    if in_str == reverse_str:
        print in_str + ' is a palindrome!'
    else:
        print in_str + ' is NOT a palindrome!'


def ispangram(in_str, alphabet=string.ascii_lowercase):
    """
    Description: Takes in a string and determines if it is a pangram (contains each letter at least once)
    :param in_str: Input string
    :param alphabet: The alphabet.
    :return: Whether or not the string is a pangram
    """

    # Create a new set and cast the string to it, removing any non-letters
    str_set = set(letter for letter in in_str if letter.isalpha())

    # str_set = [letter for letter in in_str if letter.isalpha() == True]
    # print str_set
    if len(str_set) == 26:
        print 'Looks like we have a palindrome!'
    else:
        print 'Nope... Not a palindrome :-('


# print sphere_vol(5)
# print range_check(1, 10, 10)
# case_count("Here is a sentence! Let's see what is has to offer?!?")

# lst0 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 7, 8, 9, 10, 10, 10]
# unique_list(lst0)

# lst1 = [1, 1, 1, 1, 2, 3, -4, -2, 1, -1, -1]
# multiply(lst1)

# palindrome('hohoh')

ispangram('abcdef12!@ghijklmnopqrstu$#@vwxy12345z')
