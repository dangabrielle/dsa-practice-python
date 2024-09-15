# Given a value and the root of a tree, write a function find() that returns True 
# if there is a node with the given value in the tree. Assume the tree is balanced.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(root, value):
    if not root: 
        return False
    
    if root.val == value:
        return True
    
    return find(root.left, value) or find(root.right, value)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))

print(find(root, 5)) # returns true
print(find(root, 10)) # returns false