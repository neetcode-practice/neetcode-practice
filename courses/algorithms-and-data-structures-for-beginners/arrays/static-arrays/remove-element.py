# Remove Element
# Easy
# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

# Note:

# - The order of the elements which are not equal to val does not matter.
# - It is not necessary to consider elements beyond the first k positions of the array.
# - To be accepted, the first k elements of nums must contain only elements not equal to val.

# Return k as the final result.

# Example 1:

# Input: nums = [1,1,2,3,4], val = 1

# Output: [2,3,4]
# Explanation: You should return k = 3 as we have 3 elements which are not equal to val = 1.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2

# Output: [0,1,3,0,4]
# Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # remove val from nums in-place

        # brute force: O(n), but O(n) space - space is cheap though?
        # unique_no_val = []

        # for n in nums:
        #     if n != val:
        #         unique_no_val.append(n)

        # nums[:len(unique_no_val)] = unique_no_val
        # return len(unique_no_val)
        
        # Can use two points, swap undesired values with the last value
        # decrementing with each swap

        i = 0
        # keep in mind that length is last index + 1, so decrement before read/write
        n = len(nums)

        # i --->   <---- n 
        while i < n:
            # if the value is the current index we next care to fill
            print(i, n, nums)
            if nums[i] == val:
                # decrement first so we're in bounds and then swap
                n -= 1
                nums[i] = nums[n]
            # if we don't swap, increment
            # this else protects the situation of swapping the last element
            # into the slot to fill where that element was equal to val.
            else:
                i += 1

        # when we leave the loop i and n are equal, return either
        return i

