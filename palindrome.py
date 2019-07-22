def reverseString(word):
    return word [::-1]

def isPalindrome(word):
    if len(word) < 2:
        return True
    else:
        return word == reverseString(word)