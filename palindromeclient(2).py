from palindrome import reverseString, isPalindrome #,isPalindromeRecursive

inputs = ["kayak", "hello", "abcd", "", "mom", "noon", "reverseString",
          "madam i'm adam", "never odd or even", "Was it a car or a cat I saw?", "Is this a pal?"]

print("Printing reverse strings ...")
    
for k in inputs:
    print(f"{k:30}: {reverseString(k)}")
print("-"*40)

print("Checking for palindromes ...")
for k in inputs:
    print(f"{k:30}: {isPalindrome(k)}")
print("-"*40)
##print("Checking for palindromes using recursion...")
##for k in inputs:
##    print(f"{k:30}: {isPalindromeRecursive(k)}")
##print("-"*40)
