# Given the root of a binary tree, write a function 
# that finds the value of the left most node in the tree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
         return None
    
    if not root.left:
          return root.val
    
    return left_most(root.left)
     

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
root.right = TreeNode(5)

#       1
#      /  \
#     2    5
#    /  \
#   4    3

print(left_most(root)) # returns 4

root_2 = TreeNode(1)
root_2.right = TreeNode(2)
root_2.right.left = TreeNode(3)

#       1
#        \
#         2
#        /
#       3

print(left_most(root_2)) # returns 1