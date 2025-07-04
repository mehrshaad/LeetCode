# LeetCode
# Problem: Remove Element
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-element/

from typing import List


# Solution class for the problem
class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)
