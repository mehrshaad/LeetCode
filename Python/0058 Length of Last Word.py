# LeetCode
# Problem: Length of Last Word
# Difficulty: Easy
# URL: https://leetcode.com/problems/length-of-last-word/


# Solution class for the problem
class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
