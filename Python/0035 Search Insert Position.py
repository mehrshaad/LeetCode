# LeetCode
# Problem: Search Insert Position
# Difficulty: Easy
# URL: https://leetcode.com/problems/search-insert-position/

from typing import List


# Solution class for the problem
class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target: return i
            if nums[i] > target: return i
        return len(nums)
