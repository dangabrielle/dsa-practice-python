class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ''
        for s in strs:
            output += str(len(s)) + '#' + s
        return output 

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        # initiate while loop
        # account for double digit numbers by creating a string and 
        # checking if it's a digit (separate while)
        while i < len(s):
            count = ''
            while s[i].isdigit() and i < len(s):
                count += s[i]
                i += 1
            
        # check if current character is a pound sign 
            # advance i by 1 to skip the pound
            # cut the string from i to i + number as defined in previous
            # while loop and add it to the output array
            # advance i by that amount 
            if s[i] == '#' and i < len(s):
                i += 1
                jump = int(count)
                output.append(s[i:i+jump])
                i = i + jump 
        return output
