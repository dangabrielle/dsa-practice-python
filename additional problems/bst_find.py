# Given a value and the root of a binary search tree, write a function 
# find_bst() that returns True if there is a node with the given value in 
# the tree. Assume the tree is balanced.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_bst(root, value):
    if root is None:
        return False
    
    if root.val == value:
        return True
    
    if value > root.val:
        return find_bst(root.right, value)
    elif value < root.val:
        return find_bst(root.left, value)

root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(find_bst(root, 5))
print(find_bst(root, 10))