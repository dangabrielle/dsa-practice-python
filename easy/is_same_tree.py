# Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
# Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p,q):
        # if both nodes are None, they are symmetric
        if not p and not q:
            return True
        
        # Accounts for either node being None
        if not p or not q:
            return False

        # Checks the value of the nodes
        if p.val != q.val:
            return False

        # returns true only if left and right subtrees are equal, uses depth first recursive search
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        
        

        