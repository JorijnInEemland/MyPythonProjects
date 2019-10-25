# this lecture is about for loops

# let's start by making a list to iterate over
# I'll use the range function to get the numbers 1 through 10,
# and then I'll cast that to a list
l = list(range(1, 11))
print(l)

# now, let's use a for loop to iterate over our list
for n in l:
    print(n)

# simple control flow inside the for loop
# note the use of indentation
for n in l:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is uneven")

# another example use case, again note the indentation
list_sum = 0
for n in l:
    list_sum += n
print(f"the sum of 1 through 10 is {list_sum}")

# you can iterate through strings
for letter in "Hello World":
    print(letter)

# underscore is common syntax for unused variable
for _ in range(0, 4):
    print("one two three four")

# tuple unpacking
tl = [(1,2),(3,4),(5,6)]
for a,b in tl:
    print(a+b)

# iteration through a dictionary
d = {'k1':1, 'k2':2, 'k3':3}

# normally this just gives you the keys
for k in d:
    print(k)

# here's how you iterate through the values instead
for v in d.values():
    print(v)

# you can use tuple unpacking on .items()
for k,v in d.items():
    print(f"{k} : {v}")

# remember that any order you see here is coincidence, as dictionaries are unordered

# for loops in python are always
some_iterable = range(0,3)
for item in some_iterable:
    print("do something here")
