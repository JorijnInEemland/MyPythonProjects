# while loops keep looping while something is true
a,b = 1,3
while a <= b:
    print(a)
    a += 1

# you can put else: at the end but it's kinda pointless cause it'd run anyway
else:
    print("the end")

# pass: does nothing (an empty function is not allowed in python)
if True:
    pass

# continue: skips back to the top of the current closest enclosing loop
for letter in "Hello":
    if letter == "l":
        continue
    print(letter)

# break: breaks out of the current closest enclosing loop
for letter in "Testing":
    if letter == "i":
        break
    print(letter)
