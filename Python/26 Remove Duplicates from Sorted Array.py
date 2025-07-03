# LeetCode
# Problem: Remove Duplicates from Sorted Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List


# Solution class for the problem
class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        k = len(nums)
        return k
