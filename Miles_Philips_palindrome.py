# Miles Philips
# Prog 260
# Recursive program to check if a string is a palindrome
# 7-24-19 

from string import ascii_letters

def reverseString(word):
    """returns the reverse of a string
    runtime is (O)n"""
    if len(word) < 2:
        return word
    else:
        return word [-1] + reverseString(word[:-1])

def isPalindrome(word):
    """Removes non-leters & tests whether or not a string is a palindrome
    runtime is (O)n""" 
    new = ''.join(char.lower() for char in word if char in ascii_letters)
    if len(new) < 2:
        return True
    else:
        return new[0] == new[-1] + isPalindrome(new[1:-1])
