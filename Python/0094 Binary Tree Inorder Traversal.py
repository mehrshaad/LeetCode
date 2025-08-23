# LeetCode
# Problem: Binary Tree Inorder Traversal
# Difficulty: Easy
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution class for the problem
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res
