"""
Implement all functions in only one line of code!
They should contain a single return statement.
If you think of several implementations, do them all.
No need to validate user input anywhere.
"""
from string import ascii_letters

from collections import Counter

from functools import reduce

def sum_digits(num):
    """
    Computes the sum of digits of an integer.
    """
    return sum((int(i) for i in str(num)))
        


def is_palindrome(seq):
    """
    Checks whether a given sequence is a palindrome.
    (without changing the original sequence)

    Hints:
    - there are 2 easy ways:
        - one using builtin functions
        - another using a knife
    """
    return [i for i in seq] == [i for i in reversed(seq)]


def is_gmail(string):
    """
    Checks whether a string is a Gmail email address.

    For our purposes, a valid address looks like "abcd@gmail.com".
    It must be a string of alphabetic letters (no dots) followed by '@gmail.com'.
    """
    return string.split('@')[0].isalpha() and string.split('@')[1] == 'gmail.com' 


def union(items, more_items):
    """
    Unites 2 lists/tuples into a list/tuple that contains all their elements without duplication.
    The return type must be that of the first argument `items`.
    """    

    return items + more_items if(type(items) == list) else tuple(items) + tuple(more_items)

# This is not a one-liner challenge, but should be 4 lines max
def distribution(items):
    """
    Finds how many times each item appears in a sequence of items.
    """
    #One liner:
    return (dict(zip(
        (i for i in iter(i for i in items)) , 
        (i for i in iter(items.count(i) for i in items)))))
    
# remember us? :)
formula1Champions = [
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Schumacher",
    "Alonso",
    "Alonso",
    "Räikkönen",
    "Hamilton",
    "Button",
    "Vettel",
    "Vettel",
    "Vettel",
    "Vettel",
    "Hamilton",
    "Hamilton",
    "Rosberg",
    "Hamilton",
    "Hamilton",
    "Hamilton",
    "Hamilton"
]


def all_time_champion(champions):
    """
    Finds the person has the most wins.

    Hints:
    - distribution
    - max
    - lambda
    """
    
    return max(distribution(champions).items(), key=lambda x: x[1])


def dictify(keys, values):
    """
    Creates a dict mapping the given keys to the given values.
    """
    return dict(zip(list(keys), list(values)))


def is_prime(num):
    """
    Checks whether a number is prime.

    Hints:
    - I can do this any day, and all day long!
    """
    return [i for i in range(2, num) if num % i == 0] == []

def caesar_encrypt(plain, key):
    """
    Encrypts a string using caesar cipher, with the given key as the offset.

    Hints:
    - from string import ascii_letters
    - https://www.youtube.com/watch?v=IjcX3MVSdyA
    """
    print("".join([ascii_letters[i + key] for i in [ascii_letters.find(i) for i in plain]]))


def all_time_champion2(champions):
    """
    Your previous code is cool, but now make it shorter!

    Hints:
    - from
    - collections
    - import
    - Counter
    """
    print(Counter(champions).most_common(1))
    

def factorial(num):
    """
    Computes the factorial of a number (1 * 2 * 3 * ... * num).

    Hints:
    - def factorial(num):
          '''
          Computes the factorial of a number (1 * 2 * 3 * ... * num).

          Hints:
          - ...
          '''
          pass
    """
    return 1 if num == 0 else num * factorial(num - 1)        

def compose(*funcs):
    """
    Composes all given functions.
    compose(f, g, h)(x) == f(g(h(x)))

    Hints:
    - from functools import reduce
    """
    return lambda x: reduce(lambda y, z: z(y), funcs, x)
