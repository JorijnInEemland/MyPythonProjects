# lists

# create some to do test with
list_one = ['one', 'two', 'three']
list_two = ['four', 'five', 'six']

# you can concatenate lists, do slicing, etc
print(list_one + list_two)
print(list_one[:2] + list_two[1:-1])

# lists are mutable
list_one[1] = 'CHANGED'
print(list_one)

# lists have many functions
list_two.append('seven')
print(list_two)
list_two.insert(2, 'five and a half') # the new item is inserted BEFORE the item at the index
print(list_two)
popped_item = list_two.pop() # pop removes the last item and returns it
print(list_two)
list_two.append(popped_item)
print(list_two)
list_two.pop(2) # you can set which item you want to remove
print(list_two)
removed = list_two.remove('seven') # remove finds an item and removes the first occurance
list_two.append(removed) # remove does not return anything
print(list_two)

# sort and reverse are neat
letters = ['a', 'c', 'y', 'x', 'b']
letters.sort() # sort doens't return anything
print(letters)
numbers = [4, 1, 8, 3]
numbers.reverse() # neither does reverse
print(numbers)
