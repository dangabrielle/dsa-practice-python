# Given the root of a binary tree, write a function size() that returns the number of 
# nodes in the binary tree.

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def size(root):
    if not root:
        return 0
    
    return 1 + size(root.left) + size(root.right)

node_tree = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))

#       4
#      / \
#     2   5
#    / \
#   1   3

print(size(node_tree)) # returns 5
print(size(None)) # returns 0