# LeetCode
# Problem: Longest Common Prefix
# Difficulty: Easy
# URL: https://leetcode.com/problems/longest-common-prefix/

from typing import List


# Solution class for the problem
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest
