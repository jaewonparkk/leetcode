"""
LeetCode Problem #42: Trapping Rain Water
Difficulty: Hard
URL: https://leetcode.com/problems/trapping-rain-water/

Problem Description:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Approach: Use two pointers from both ends, tracking max heights.
        Water trapped at each position = min(max_left, max_right) - current_height
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
        
        return water
    
    def trap_dp(self, height: list[int]) -> int:
        """
        Alternative solution using Dynamic Programming
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        # Fill left_max array
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Fill right_max array
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Calculate water
        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
        
        return water


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result1 = solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(f"Test case 1: {result1} (Expected: 6)")
    assert result1 == 6
    
    # Test case 2
    result2 = solution.trap([4, 2, 0, 3, 2, 5])
    print(f"Test case 2: {result2} (Expected: 9)")
    assert result2 == 9
    
    # Test DP solution
    result3 = solution.trap_dp([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(f"Test case 3 (DP): {result3} (Expected: 6)")
    assert result3 == 6
    
    print("All test cases passed!")
