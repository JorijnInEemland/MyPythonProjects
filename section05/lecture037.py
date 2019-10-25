# Statements Assessment Test

# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for w in st.split():
    if w[0].lower() == 's':
        print(w)

# Use range() to print all the even numbers from 0 to 10.
# I'm assuming they mean including 10 here.
print(list(range(0,11,2)))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([x for x in range(1,51) if x % 3 == 0])

# Go through the string below and if the length of a word is even print "even!"
# The string is asking something different than the exercise? I'll do that cause it'll give a more useful result.
st = 'Print every word in this sentence that has an even number of letters'
for w in st.split():
    if len(w) % 2 == 0:
        print(w)

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(1, 101):
    three = x % 3 == 0
    five = x % 5 == 0
    if three and five:
        print("FizzBuzz")
    elif three:
        print("Fizz")
    elif five:
        print("Buzz")
    else:
        print(x)

# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
l = [w[0] for w in st.split()]
print(l)

# I got everything right, though I had to google how to get the length of a string cause I forgot about len()
