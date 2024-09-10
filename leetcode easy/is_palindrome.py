# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. 
# It is also case-insensitive and ignores all non-alphanumeric characters.

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # re is a python lib that allows regex manipulation of strings 
        # r' ' : tells python to treat it as a raw string (not interpret backslashes '\' as escaping)
        # re.sub : substitute / replace method
        # ^ : considers all characters except for what's denoted (only takes in alpha numeric)
        new_s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        start, end = 0, len(new_s) - 1
        # loop through new_s using two pointer technique and check if each char are equal
        # if not, then it is not a palindrome 
        while start <= end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True
