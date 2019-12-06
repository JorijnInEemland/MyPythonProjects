# Functions and Methods - Homework Assignment

# Import the necessary stuff
import math
import string

# Calculate the volume of a sphere given its radius
def vol(rad):
    return (4 / 3) * (math.pi) * (rad ** 3)

# Check whether a number is in a given range
def is_in_range(num, low, high):
    return low <= num <= high

print(f"10 {'is' if is_in_range(10, 5, 15) else 'is not'} in range 5 to 15")
print(f"5 {'is' if is_in_range(5, 10, 15) else 'is not'} in range 10 to 15")

# Count the amount of upper and lower case letters in a string
# I tried to find how to do it with the collections module but couldn't
def count_upper_lower(s):
    u = len(list(filter(lambda c: c.isupper(), s)))
    l = len(list(filter(lambda c: c.islower(), s)))
    return u, l

rogers = count_upper_lower('Hello Mr. Rogers, how are you this fine Tuesday?')
print(f"Number of upper case characters : {rogers[0]}")
print(f"Number of lower case characters : {rogers[1]}")

# Check whether a string is a palindrome
def palindrome(s):
    s = list(filter(lambda c: c in string.ascii_letters, s.lower()))
    return s == s[::-1]

print(f"'madam' {'is' if palindrome('madam') else 'is not'} a palindrome")
print(f"'madamme' {'is' if palindrome('madamme') else 'is not'} a palindrome")
print(f"'nurses run' {'is' if palindrome('nurses run') else 'is not'} a palindrome")
print(f"'nurses walk' {'is' if palindrome('nurses walk') else 'is not'} a palindrome")

# Check whether a string has every letter of the alphabet
def pangram(s):
    return not len(list(filter(lambda c: not c in s.lower(), string.ascii_lowercase)))

print(f"'ewcpewtvnpuweipm' {'is' if pangram('ewcpewtvnpuweipm') else 'is not'} a pangram")
print(f"'abcdefghijklmnopqrstuvwxyz' {'is' if pangram('abcdefghijklmnopqrstuvwxyz') else 'is not'} a pangram")
