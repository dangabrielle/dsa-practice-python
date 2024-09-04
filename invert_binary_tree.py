# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root):
        if not root:
            return None

        # swap nodes
        root.left, root.right = root.right, root.left

        # continue to do depth first traversal
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
        