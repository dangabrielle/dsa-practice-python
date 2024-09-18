# Write a function linear_search() to help Winnie the Pooh locate his lost 
# items. The function accepts a list items and a target value as parameters. 
# The function should return the first index of target in items, and -1 if 
# target is not in the lst. Do not use any built-in functions.

def linear_search(lst, target):
    for idx, str in enumerate(lst):
        if str == target:
            return idx
        
    return -1



items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
print(linear_search(items, target)) # returns 3

items1 = ['bed', 'blue jacket', 'red shirt', 'hunny']
target1 = 'red balloon'
print(linear_search(items1, target1)) # returns -1