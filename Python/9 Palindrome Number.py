# LeetCode
# Problem: Palindrome Number
# Difficulty: Easy
# URL: https://leetcode.com/problems/palindrome-number/


# Solution class for the problem
class Solution:

    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
