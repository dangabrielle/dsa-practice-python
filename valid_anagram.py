# Given two strings s and t, return true if the two strings 
# are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters 
# as another string, but the order of the characters can be different.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case to handle input strings of diff length
        if len(s) != len(t):
            return False

        # to get freq count of first str, s
        s_freq = {}

        for char_s in s:
            if char_s in s_freq:
                s_freq[char_s] += 1
            else:
                s_freq[char_s] = 1

        # loop through the second str, t
        # if char is in the freq count, subtract its value by 1
        for char_t in t:
            # to avoid negative values, ensure value in s_freq > 0
            if char_t in s_freq and s_freq[char_t] > 0:
                s_freq[char_t] -= 1
            else:
                return False
        
        # this will be reached after going through each char in string t
        return True