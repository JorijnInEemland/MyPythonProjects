my_string = "Hello World"
print(my_string[0])
print(my_string[8])
print(my_string[-3]) # with negative indexing, -1 is the last character

alphabet = "abcdef"
print(alphabet[3:]) # the first element is 0, so the fourth element is 3
print(alphabet[:3]) # remember slicing is up to but not including the stop index
print(alphabet[2:4]) # 4 - 2 = 2, the amount of characters this returns
print(alphabet[::2]) # use the step size to grab for example every other character
print(alphabet[::-1]) # use a negative step size to reverse the string
