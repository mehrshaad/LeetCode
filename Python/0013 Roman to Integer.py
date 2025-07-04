# LeetCode
# Problem: Roman to Integer
# Difficulty: Easy
# URL: https://leetcode.com/problems/roman-to-integer/


# Solution class for the problem
class Solution:

    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            curr_value = values[char]
            if curr_value >= prev_value:
                total += curr_value
            else:
                total -= curr_value
            prev_value = curr_value

        return total
