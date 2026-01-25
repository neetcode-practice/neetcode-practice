# Remove Duplicates From Sorted Array
# Easy
# You are given an integer array nums sorted in non-decreasing order. Your task is to remove 
# duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that 
# the first k elements of nums contain the unique elements.

# Note:

# - The order of the unique elements should remain the same as in the original array.
# - It is not necessary to consider elements beyond the first k positions of the array.
# - To be accepted, the first k elements of nums must contain all the unique elements.

# Return k as the final result.

# Example 1:

# Input: nums = [1,1,2,3,4]

# Output: [1,2,3,4]
# Explanation: You should return k = 4 as we have four unique elements.

# Example 2:

# Input: nums = [2,10,10,30,30,30]

# Output: [2,10,30]
# Explanation: You should return k = 3 as we have three unique elements.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n^2)
        # # start at the end of the array
        # i = len(nums) - 1

        # while i > 0:
        #     # if the value before last equals the previous value, pop current            
        #     if nums[i - 1] == nums[i]:
        #         nums.pop(i)

        #     # always decrement
        #     i -= 1

        # return len(nums)

        # O(n log (n))
        # sets are in any order they want
        # unique = set(nums)
        # therefore, we need to sort after making the set.
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)
    
