# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create pointers to traverse through list1 and list2
        l1 = list1
        l2 = list2
        # Create a temporary node as the start of the combined list 
        temp = ListNode(-1)
        current = temp

        # As long as either list1 or list2 are not None, traverse through each list
        # and add to the newly combined list as long as it's in ascending order 
        while l1 and l2:
            # Check to see which node has the smaller value, then add to combined list 
            if l1.val < l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next
        
        # to account for unequal list lengths, add the longer list 
        # to the end of 'current'
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        
        # return combined list, minus the initial temp node
        return temp.next