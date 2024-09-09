# Given the root of a binary tree, return true if it is a valid binary search tree, 
# otherwise return false.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Perform an in-order traversal (left, root, right).
# Make sure all nodes in the left subtree are less than the current node.
# For the entire tree to be a valid BST, if any node 
# is found to be less than or equal to the previous node (the node that was 
# visited immediately before the current node), then it is not a BST

class Solution:
    def __init__(self):
        self.prev = float('-inf')

    def isValidBST(self, root):
       return self.inorder(root)
       

    def inorder(self, node):
        # base case if tree is empty, if leaf nodes are reached
        if not node:
            return True
        
        # recursively traverse the left subtree. All nodes in this subtree 
        # must have values less than the current node otherwise return false
        if not self.inorder(node.left):
            return False

         # Check if current node's value is greater than 
         # the previous node's value
        if node.val <= self.prev:
            return False

        # If the current node is valid (i.e., greater than the previously 
        # visited node), update the prev variable to the current node's value.
        self.prev = node.val

        # recursively traverse the right subtree, ensuring all nodes in this subtree 
        # are greater than the current node.
        return self.inorder(node.right)
    
        

            
        


        