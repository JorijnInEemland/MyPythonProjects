name = "Sam"
# name[0] = 'P'
# this doesn't work, because strings are immutable, can not mutate
name = "Pam"
# this does work, because we're discarding the whole previous value
print(name)

# example of string concatenation
end = name[1:]
name = 'H' + end
print(name)

# you can use multiplication with strings
z = 'z'
sleep = z * 10
print(sleep)

# strings have many functions
x = "Hello World"
print(x.upper())
print(x.lower())
print(x.swapcase().replace(' ', '_'))

# split(your_split_char) is pretty neat (space by default)
x = "This is a string."
for s in x.split():
    print(s)
