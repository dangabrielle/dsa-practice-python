# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums):
         # Convert nums (arr) into a set, which will remove duplicate values
         set_nums = set(nums)

         # Compare the length of nums with the length of the set
         # If unequal, then a duplicate is present
         if len(set_nums) == len(nums):
            return False
         else:
            return True
