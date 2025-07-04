# LeetCode
# Problem: Plus One
# Difficulty: Easy
# URL: https://leetcode.com/problems/plus-one/

from typing import List


# Solution class for the problem
class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        ans = int("".join(map(str, digits))) + 1
        return [int(digit) for digit in str(ans)]
