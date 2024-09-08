# Given a binary tree root, return the level order traversal of it as a nested list, 
# where each sublist contains the values of nodes at a particular level in the tree,
#  from left to right.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# python uses deque class to create queues, as it optimizes time complexity to a 
# O(1) for removing nodes from the beginning of the queue and O(1) to add nodes
# to the end of a queue, as opposed to using a normal list
from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        
        # initialize deque object
        queue = deque()
        queue.append(root)
        output = []

        # queues utilize first in first out approach and is line with the
        # breadth first approach, aka level order traversal. This means that 
        # child nodes are added based on level. To solve this problem, loop through
        # the queue (as long as it is not empty) and add nodes in the queue to an
        # array (level_nodes). This will be added to the output array.
        # Append their children to the queue (if there are any)
        # and continue through the loop
        while queue:
            level_nodes = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(level_nodes)
        return output