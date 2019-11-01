# Simple function definition
def name_of_function(argument):
    '''docstring exlaining the function'''
    print(f'do something here, perhaps using the {argument}')
    return "something, or don't"

# Use help() to get the docstring
help(name_of_function)

# Default value for argument, return something
def say_hello(name='Name Here'):
    return f'Hello {name}!'

# Use our function
print(say_hello())

# Find out if the word "dog" is in a string
def dog_check(mystring):
    return 'dog' in mystring.lower()

print(dog_check('Dogs say meow'))
print(dog_check('Cats say woof'))

# If the word starts with a consonant, move it to the end
# Then add 'ay' to the end of the word
def pig_latin(word):
    if word[0].lower() in 'aeiou':
        return word + 'ay'
    else:
        return word[1:] + word[0] + 'ay'

    # Or by redefining the variable locally:
    # if word[0].lower() in 'aeiou':
    #     word = word[1:] + word[0]
    # return word + 'ay'

    # Or as a single line:
    # return word + 'ay' if word[0] in 'aeiou' else word[1:] + word[0] + 'ay'

print(pig_latin('word'))
print(pig_latin('apple'))
