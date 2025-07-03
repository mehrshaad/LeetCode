# LeetCode
# Problem: Valid Parentheses
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-parentheses/


# Solution class for the problem
class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in '({[':
                stack.append(p)
                continue
            try:
                if (p == ')' and stack[-1]
                        == '(') or (p == ']' and stack[-1]
                                    == '[') or (p == '}' and stack[-1] == '{'):
                    stack.pop()
                else:
                    return False
            except:
                return False
        if stack == []:
            return True
        return False
