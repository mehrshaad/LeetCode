# LeetCode
# Problem: Sqrt(x)
# Difficulty: Easy
# URL: https://leetcode.com/problems/sqrtx/

from math import floor


# Solution class for the problem
class Solution:

    def mySqrt(self, x: int) -> int:
        return floor(x**0.5)
