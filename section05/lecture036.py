# misc operators

# you can use range as a substitute for traditional for loops
for i in range(3):
    print(i)

# range can take start, stop, and step
range_string = ""
for i in range(6,16,3):
    range_string = f"{range_string},{i}"
print(range_string[1:])

# range is a generator meaning it doesn't store the result in memory
print(range(6,16,3))
# if you want it as a list you have to cast
print(list(range(6,16,3)))

# enumerate is very useful if you need to know the index of the current item
for i,l in enumerate('abdce'):
    print(f'index {i} has letter {l}')

# zip combines multiple iterables like a zipper
# the result is the length of the shortest iterable times two
# it's a generator that gives you a list of tuples
print(list(zip('abcd', '123456', '!@#$')))

# you can use `in` to check if an object is in an iterable
print(f"is 'x' in 'abc'? {'yes' if 'x' in 'abc' else 'no'}")
print(f"is 'x' in 'xyz'? {'yes' if 'x' in 'xyz' else 'no'}")

# use min and max to find the lowest and highest values in an iterable
mylist = [20, 40, 10, 30]
print(min(mylist))
print(max(mylist))

# import a whole file, usually discouraged
# use `from foo import bar` to import only a piece
import math

# shuffle doesn't return anything, shuffles the list in place
from random import shuffle
mylist = [1,2,3,4,5]
print(mylist)
shuffle(mylist)
print(mylist)
shuffle(mylist)
print(mylist)

# randint generates a random integer in the given range, not random enough for encryption
# up to and including the end number (this is different from range())
from random import randint
print(randint(1,10))

# input prints the input and returns a string
i = input('enter something: ')

# list comprehensions are a unique way of quickly creating a list with python
mystring = i
mylist = []

# here's the usual way to do it
for letter in mystring:
    if not letter in '1234567890':
        mylist.append(letter.capitalize())

# here's the python one-liner way
# this is really hard to read though lol, don't use this
mylist = [letter.capitalize() for letter in mystring if not letter in '1234567890']
print(mylist)

# you can do if else inside list comprehension too but please just don't
print([x if x%2==0 else 'odd' for x in range(11)])

# oh god nested loop inside list comprehension why
print([x*y for x in [1, 2, 3] for y in [1, 10, 100]])
