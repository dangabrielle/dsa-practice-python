# Reverse a Linked List
# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Solution (iterative):

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        # Traverse through the linked list and use a two pointer technique 
        # Pointer 1: track the current node as you're traversing, Pointer 2: a previous pointer initially set to None
        prev = None
        current = head

        # Example input: 1 -> 2 -> 3 -> None 
        # Expected outpout: None <- 1 <- 2 <- 3
        while current:
            # Store current's next node (2)
            next_node = current.next
            # Break the link between 1 -> 2 and instead point 1 -> prev (None)
            current.next = prev
            # Set prev to the current node 
            prev = current
            # Continue on through the list by setting current = next_node stored earlier 
            current = next_node
        # prev now has the head of the reversed list 
        return prev