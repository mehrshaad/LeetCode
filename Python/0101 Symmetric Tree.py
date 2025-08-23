# LeetCode
# Problem: Symmetric Tree
# Difficulty: Easy
# URL: https://leetcode.com/problems/symmetric-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution class for the problem
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isMirror(left: Optional[TreeNode],
                     right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(
                left.right, right.left)

        return isMirror(root.left, root.right) if root else True
