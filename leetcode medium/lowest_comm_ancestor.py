# Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, 
# return the lowest common ancestor (LCA) of the two nodes.

# The lowest common ancestor between two nodes p and q is the 
# lowest node in a tree T such that both p and q as descendants. 
# The ancestor is allowed to be a descendant of itself.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # used as a pointer to traverse through the tree
        curr = root

        while curr:
            # since this is a BST, you can traverse through either the
            # left or right side depending on where p and q reside

            # if p and q are greater than the root val, search right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = root.right

            # if p and q are less than the root val, search left
            elif p.val < curr.val and q.val < curr.val:
                curr = root.left

            # if p and q are on different sides, then the root node is the LCA 
                # p < root and q > root, or vice versa 
            # if p or q is equal to the root, then either one of them is the LCA
            # no need to have a return outside of the loop because this case will always hit
            else:
                return curr