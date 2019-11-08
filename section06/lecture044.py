# Complete-Python-3-Bootcamp/03-Methods and Functions/03-Function Practice Exercises.ipynb

# Lesser of two evens
def lesser_of_two_evens(a, b):
    # If one or both are uneven
    if a % 2 or b % 2:
        # Return the larger number
        return a if a > b else b
    # Else if both are even
    else:
        # Return the smaller number
        return a if a < b else b

# Testing
print("Lesser of two evens:")
print(f"    {lesser_of_two_evens(2,4)}")
print(f"    {lesser_of_two_evens(2,5)}")
print(f"    {lesser_of_two_evens(3,7)}")

# Animal crackers
def animal_crackers(words):
    words = words.lower().split()
    if len(words) > 1 and words[0][0] == words[1][0]:
        return True
    else:
        return False

# Testing
print("Animal Crackers:")
print(f"    {animal_crackers('Levelheaded Llama')}")
print(f"    {animal_crackers('Crazy Kangaroo')}")

# Other side of seven
def other_side_of_seven(number):
    return 7 + (2 * (7 - number))

# Testing
print("Other side of seven:")
print(f"    {other_side_of_seven(4)}")
print(f"    {other_side_of_seven(12)}")

# Makes twenty
def makes_twenty(a, b):
    return a == 20 or b == 20 or a + b == 20

# Testing
print("Makes twenty:")
print(f"    {makes_twenty(20, 10)}")
print(f"    {makes_twenty(12, 8)}")
print(f"    {makes_twenty(2, 3)}")

# Old macdonald
def old_macdonald(name):
    if len(name) < 4:
        return "Name too short"
    new_name = []
    for index, letter in enumerate(name.lower()):
        if index == 0 or index == 3:
            new_name.append(letter.capitalize())
        else:
            new_name.append(letter)
    return "".join(new_name)

# Testing
print("Old macdonald:")
print(f"    {old_macdonald('mAcDoNaLd')}")

# Master yoda
def master_yoda(sentence):
    new_sentence = []
    for word in sentence.split()[::-1]:
        new_sentence.append(word)
        new_sentence.append(' ')
    return ''.join(new_sentence[:-1])

# Testing
print("Master yoda:")
print(f"    {master_yoda('I am home')}")

# Almost there
def almost_there(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

# Testing
print("Almost there:")
print(f"    {almost_there(105)}")
print(f"    {almost_there(150)}")
print(f"    {almost_there(190)}")

# Find 33
def has_33(mylist):
    for index, integer in enumerate(mylist):
        if index == len(mylist) - 1:
            return False
        if integer == mylist[index + 1] == 3:
            return True

# Testing
print('Find 33:')
print(f"    {has_33([1, 3, 3])}")
print(f"    {has_33([1, 3, 1])}")
print(f"    {has_33([3, 1, 3])}")

# Paper doll
def paper_doll(text):
    return ''.join([char * 3 for char in text])

# Testing
print("Paper doll:")
print(f"    {paper_doll('Hello')}")

# Blackjack
def blackjack(a, b, c):
    abc = a + b + c
    if abc <= 21:
        return abc
    if a == 11 or b == 11 or c == 11:
        abc -= 10
    return abc if abc <= 21 else 'BUST'

# Testing
print("Blackjack:")
print(f"    {blackjack(5, 6, 7)}")
print(f"    {blackjack(9, 9, 9)}")
print(f"    {blackjack(9, 10, 11)}")

# Summer of '69
def summer_of_69(array):
    summer = status = 0
    for item in array:
        if item == 6 or item == 9:
            status = item
        if status == 6:
            continue
        if status == 9:
            status = 0
            continue
        summer += item
    return summer

# Testing
print("Summer of '69:")
print(f"    {summer_of_69([1, 3, 5, 6, 8])}")
print(f"    {summer_of_69([4, 5, 6, 7, 9, 10])}")

# Spy game
def spy_game(numbers):
    for index in range(len(numbers)):
        if index > len(numbers) - 3:
            return False
        if numbers[index : index + 3] == [0, 0, 7]:
            return True

# Testing
print("Spy game:")
print(f"    {spy_game([1,2,4,0,0,7,5])}")
print(f"    {spy_game([1,0,2,4,0,5,7])}")
print(f"    {spy_game([1,7,2,0,4,5,0])}")
print(f"    {spy_game([1,3,5,9,0,0,7])}")

# Count primes
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def count_primes(num):
    count = 0
    for x in range(2, num + 1):
        if is_prime(x):
            count += 1
    return count

# Testing
print("Count primes:")
print(f"    {count_primes(100)}")

# There's an exercise where you have to print the given letter as a 5x5 pattern of asterix characters, but I can't be bothered
print("Great job me")
