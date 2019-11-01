# *args and **kwargs

# Use *argument_name to get as many inputs as you want
# PEP8 says it should always be called *args
def summer(*args):
    return sum(args)

# It takes all the parameteres and combines them into a tuple
print(summer(1,2,3,4,5))

# Use **keyword_argument_name to get as many keyworded arguments as you want
# PEP8 says it should always be called **kwargs
def fruiter(**kwargs):
    # You can find a keyword like this
    if 'fruit' in kwargs:
        # And get its value like this
        print(f"My fruit of choice is {kwargs['fruit']}")
    else:
        print("No fruit here")

# It takes all the keyword argumens and combines them into a dictionary
fruiter(fruit='apple')
fruiter(vegeta='kakarot')

# You can use *args and **kwargs in the same function
def bigfunc(*args, **kwargs):
    print(f"I would like {args[0]} instances of food item {kwargs['food']}")
    print(f"I would like {args[1]} instances of drink item {kwargs['drink']}")

# Very cool
bigfunc(5, 8, drink='soup', food='bread')
