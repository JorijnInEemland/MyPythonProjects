# sets are unordered collections of unique elements
# meaning there can only be one of each object

# you create a set using set()
s = set()
print(s)

# you can add items with .add()
s.add(1)
s.add(2)
print(s)

# adding duplicate items is ignored
s.add(2)
print(s)

# you can cast a list to a set
l = [1, 2, 2, 3, 3, 3]
s = set(l)
print(s) # this might look ordered, but that's only coincidence
