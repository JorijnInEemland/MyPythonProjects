# dictionaries use { curly brackets } and : colons
# they are unordered, and can not be sorted

# use example
my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])

# purpose example
prices = {'apple':2.99, 'orange':1.99, 'water':9.99}
print(f"apples cost ${prices['apple']} each")

# values can be anything
d = {'k1':123, 'k2':[0,1,2], 'k3':{'one':'abc', 'two':'def'}}
print(d['k3']['one'].upper())

# keys can be strings or numbers
d = {'one':1, 5:'five'}
print(d)

# dictionaries are mutable, and you can easily add things
d = {'k1':'one hundred', 'k2':200}
d['k1'] = 100
d['k3'] = 300

# here's how you get keys, values, and pairs
print(d.keys())
print(d.values())
print(d.items())
