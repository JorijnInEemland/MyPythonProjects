# tuples are lists but immutable
# the syntax is ( parenthesis )

# list
l = [1,2,3]
l[0] = 5 # you can do this
print(type(l))
print(l)

# tuple
t = (1,2,3)
# t[0] = 5 # you can't do this
print(type(t))
print(t)

# tuples only have two methods, a lot less than lists
t = ('a', 'a', 'b', 'b', 'c', 'c')
print(f"the amount of instances of the character 'a' in the tuple is {t.count('a')}")
print(f"the first index in the tuple that has the character 'c' is {t.index('c')}")
