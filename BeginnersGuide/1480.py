"""
Running Sum of a 1D array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            nums[i] = current_sum
        return nums
