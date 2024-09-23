# Given an array nums with n integers, write a function non_decreasing() that checks
# if nums could become non-decreasing by modifying at most one element.

# We define an array is non-decreasing if nums[i] <= nums[i + 1] 
# holds for every i (0-based) such that (0 <= i <= n - 2).
# meaning: each element in the array must be greater than or equal to its
# previous element

def non_decreasing(nums):
    num_modif = 0

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            # keep track of number of modifications
            num_modif += 1
            # if there is more than 1 modification, return false
            if num_modif > 1:
                return False

            # attempt the modification 
            # if this is the first element, set it to 
            # the value of the next element
            if i == 0:
                nums[i] = nums[i + 1]
            # if it's a middle element, and the prev element (at i - 1) is 
            # less than or equal to the next element (at i + 1), then 
            # we can modify nums[i] and make it equal to the element at i + 1
            elif nums[i-1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
            # if it's a middle element, but the next value is greater than
            # or equal to the previous, set the next value to the current value
            elif nums[i+1] >= nums[i-1]:
                nums[i+1] = nums[i]

    return True

nums = [4, 2, 3] 
print(non_decreasing(nums)) # true

nums = [4, 2, 1]
print(non_decreasing(nums)) # false