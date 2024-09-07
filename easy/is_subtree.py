# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root, subRoot):
        # None will always be a subtree (consider leaf nodes' .left and .right)
        if not subRoot:
            return True 
        
        # if root is None, then there's no possible way subRoot is a subtree
        if not root:
            return False
        
        # used to check if trees are the same
        if self.isSameTree(root, subRoot):
            return True

        # continually check root's left and right subtrees and compare if it is the 
        # same tree as subRoot
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # helper function to check if root's subtree is the same as input subtree
    def isSameTree(self, r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r and s and r.val == s.val:
                return self.isSameTree(r.left, s.left) and self.isSameTree(r.right, s.right)