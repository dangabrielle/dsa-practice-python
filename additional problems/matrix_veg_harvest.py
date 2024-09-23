# Rabbit is collecting carrots from his garden to make a feast for Pooh and
# friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch
#  and returns the number of of carrots that are ready to harvest in the vegetable patch. 
# A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.

# Assume n = len(vegetable_patch) and 
# m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.

def harvest(vegetable_patch):
	count = 0
	for i in range(len(vegetable_patch)):
		for j in range(len(vegetable_patch[i])):
			if vegetable_patch[i][j] == 'c':
				count += 1
	return count


vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
print(harvest(vegetable_patch)) # 6

vegetable_patch_2 = [ 
	['x', 'x', 'x'],
	['x', 'x', 'x'],
	['x', 'x', 'x'],
	['x', 'x', 'x']
]
print(harvest(vegetable_patch_2)) # 0
print(harvest([])) # 0