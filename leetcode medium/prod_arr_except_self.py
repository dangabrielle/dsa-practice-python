# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute force
        # output = []
        # i = 0
       
        # while i < len(nums):
        #     if i == 0:
        #         output.append(math.prod(nums[i + 1:]))
              
        #     elif i == len(nums) - 1:
        #         output.append(math.prod(nums[:-1]))
          
        #     else:
        #         output.append(math.prod(nums[:i]) * math.prod(nums[i + 1:]))
        #     i += 1
        # return output
            
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            else: 
                prod *= num
        if zeros > 1: return [0] * len(nums)

        output = []
        for num in nums:
            if 0 in nums:
                if num == 0:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                output.append(int(prod / num))

        return output