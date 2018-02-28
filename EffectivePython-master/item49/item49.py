# words.py
"""Library for test word utility

This module can use to test simple word's ability

Avaliable functions:
- palindrome
"""


def palindrome(word):
    """return true if word is palindrome"""
    return word == word[::-1]


if __name__ == '__main__':
    print(palindrome.__doc__)
