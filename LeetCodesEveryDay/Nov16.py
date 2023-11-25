##Problem 1: EASY

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
    
        # Iterate through the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if the complement is in the dictionary
            if complement in num_dict:
                # If found, return the indices of the two numbers
                return [num_dict[complement], i]
            
            # If the complement is not in the dictionary, add the current number to it
            num_dict[num] = i
        
        # If no solution is found, return an empty list or raise an exception
        return []
