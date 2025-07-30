# LeetCode
# Problem: Count Hills and Valleys in an Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

from typing import List


# Solution class for the problem
class Solution:

    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        nums = self.removeDuplicates(nums)
        for i in range(len(nums)):
            if i == len(nums) - 1 or i == 0:
                continue
            if (nums[i] > nums[i - 1]
                    and nums[i] > nums[i + 1]) or (nums[i] < nums[i - 1]
                                                   and nums[i] < nums[i + 1]):
                ans += 1
        return ans

    def removeDuplicates(self, lst: List[int]) -> List[int]:
        if not lst:
            return []

        result = [lst[0]]
        for item in lst[1:]:
            if item != result[-1]:
                result.append(item)
        return result
