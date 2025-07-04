# LeetCode
# Problem: Add to Array-Form of Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import List


# Solution class for the problem
class Solution:

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)

        while k:
            k, digit = divmod(k, 10)
            num.insert(0, digit)

        return num
