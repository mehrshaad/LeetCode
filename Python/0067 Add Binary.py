# LeetCode
# Problem: Add Binary
# Difficulty: Easy
# URL: https://leetcode.com/problems/add-binary/


# Solution class for the problem
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
