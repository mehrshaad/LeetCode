# LeetCode
# Problem: Merge Sorted Array
# Difficulty: Easy
# URL: https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import List


# Solution class for the problem
class Solution:

    def merge(self, nums1: List[int], m: int, nums2: List[int],
              n: int) -> None:
        nums1[:] = list(sorted(nums1[:m] + nums2[:n]))
