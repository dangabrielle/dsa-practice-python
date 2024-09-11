# If you implemented the previous left_most() function iteratively, implement it 
# recursively. If you implemented it recursively, implement it iteratively.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    
    curr = root

    while curr.left:
        curr = curr.left
    
    return curr.val


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