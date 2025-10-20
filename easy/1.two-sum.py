"""
LeetCode Problem #1: Two Sum
Difficulty: Easy
URL: https://leetcode.com/problems/two-sum/

Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Approach: Use a hash map to store the complement of each number.
        """
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("Test case 1 passed!")
    
    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    print("Test case 2 passed!")
    
    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("Test case 3 passed!")
    
    print("All test cases passed!")
