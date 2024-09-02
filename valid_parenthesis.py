# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:
        # account for single char input, ie '['
        if len(s) == 1:
            return False

        brackets = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }
        
        stack = []

        for char in s:
            # if char in brackets, append its corresponding closing bracket to the stack
            if char in brackets:
                stack.append(brackets[char])
            # if char is a closing bracket, only pop the stack if its not empty and char == last
            # element in the stack
            elif char in brackets.values():
                if len(stack) > 0 and char == stack[-1]:
                    stack.pop()
                # account for input when it's only closing brackets ie ']]'
                else:
                    return False
        
        # if the stack is empty, then all brackets were matched 
        return len(stack) == 0