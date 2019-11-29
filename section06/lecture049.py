# Lambda Expressions, Map, and Filter

# map() can be used with any iterable
# The function you pass in doesn't get executed right away, but when you iterate through it

# Some math distraction

# Numbers 1 through 9
nums = [1,2,3,4,5,6,7,8,9]
print(nums)

# Squares of those numbers
def square(num):
    return num**2
sqrs = list(map(square,nums))
print(sqrs)

# Difference between each square and the one before it
new = []
for i in range(len(sqrs)):
    new.append(sqrs[i] - sqrs[i-1])
new[0] = 0
print(new)

# Neat right?

# Anyway uh let's continue the lecture

# filter() is like map() but the resulting iterable will have only items that pass the condition set in the provided function

def check_even(num):
    return num % 2 == 0
print(list(filter(check_even, nums)))

# Now, lambda expressions

# Lambda to square every number in a list
print(list(map(lambda num: num**2, nums)))

# Lambda to filter only even numbers
print(list(filter(lambda num: num%2==0, nums)))

# Lambda to get the first character of a string
names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda name: name[0], names)))
