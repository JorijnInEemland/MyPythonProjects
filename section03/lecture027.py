# basic file I/O, big lecture

# making the file that's used below
# modes: r = read, w = write, a = append, r+ = read and write w+ = write and read
# w and w+ overwrite existing files, and can make new files
with open('../files/test.txt', mode='w') as myfile:
    content = [
        'Hello this is a text file\n',
        'This is the second line\n',
        'This is the third line']
    myfile.writelines(content)

# you open files with open()
# both relative and absolute paths work
# don't bother with \\ because / works everywhere
myfile = open('../files/test.txt')

# you can grab the whole file with .read()
print('example of .read()')
print(myfile.read())
# but when you do, it moves the read index to the end
# so to read again you'll have to set it back to the start
myfile.seek(0)
print('--------------------')

# you can read files line by line with a for loop
print('example of for each loop')
for line in myfile:
    print(line)
myfile.seek(0)
print('--------------------')

# or with .readline()
print('example of .readline()')
print(myfile.readline())
myfile.seek(0)
print('--------------------')

# or get the whole file as a list of lines with .readlines()
print('example of .readlines()')
print(myfile.readlines())
myfile.seek(0)
print('--------------------')

# you close files with .close()
myfile.close()

# you can also use the with statement
# then you don't need to manually close the file
with open('../files/test.txt') as myfile:
    print(myfile.read())
