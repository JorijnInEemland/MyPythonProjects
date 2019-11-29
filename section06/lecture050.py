# Nested Statements and Scope

x = 25

def loc():
    x = 50
    return x

# Don't use globals unless absolutely necessary

def glo():
    global x
    x = 50
    return x

print(f'  x: {x}')
print(f'loc: {loc()}')
print(f'  x: {x}')
print(f'glo: {glo()}')
print(f'  x: {x}')

# You can put functions in functions

def one():
    def two():
        print("two")

    print("one")

    two()

one()
