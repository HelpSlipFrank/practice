"""
http://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
Ask the user for a string and print out whether this string is a palindrome or not.

"""

def palindrome():

    while True:
        str = raw_input("If you give me a word, I'll let you know if it's a palindrome. So, what's the word? ")
        if str == str[::-1]:
            print("That's pretty cool! '%s' is a palindrome!" % (str))
        else:
            print("That's a negatory, Ghostrider. '%s' is not a palindrome." % (str))

        loop = raw_input("Wanna try again?")
        if loop.lower() == 'y' or loop.lower() == 'yes':
            continue
        else:
            break

palindrome()