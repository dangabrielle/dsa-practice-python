# Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. 
# In an inorder traversal we traverse the left subtree, then the current node, 
# then the right subtree.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
    output = []
    # pass list reference to helper function 
    # any changes made will persist since lists are mutable
    dfs(root, output)

    # when recursion ends, output array will contain all values in the 
    # in-order traversal, which you can then return 
    return output
    
# recursive helper function that performs depth first traversal 
# will first go down to the left subtree until leaf node is visited
# if node is not None, recursively visit the left subtree,
# append the value of the current node, and then recursively visit the
# right subtree
def dfs(node, arr):
    if not node:
        return None
    
    dfs(node.left, arr)
    arr.append(node.val)
    dfs(node.right, arr)
      

node_1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))

#       1
#         \
#          2
#         /
#        3

print(inorder_traversal(node_1))
print(inorder_traversal(None))
print(inorder_traversal(TreeNode(1)))