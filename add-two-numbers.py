# LeetCode
# Problem: Add Two Numbers
# Difficulty: Medium
# URL: https://leetcode.com/problems/add-two-numbers/

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution class for the problem
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.listNodeToList(l1)
        n2 = self.listNodeToList(l2)
        ans = n1 + n2
        ans = [int(i) for i in str(ans)][::-1]
        self.ansLen = len(ans)
        ans = self.createListNode(ans, 0)
        return ans

    def listNodeToList(self, ln: Optional[ListNode]):
        ls = []
        while ln:
            ls.append(str(ln.val))
            ln = ln.next
        ls = reversed(ls)
        return int("".join(ls))

    def createListNode(self, ls: list, i: int, nxt=None):
        if i >= self.ansLen:
            return
        val = ls[0]
        return ListNode(
            val,
            self.createListNode(ls=ls[1:],
                                i=i + 1,
                                nxt=ListNode(val=val, next=nxt)),
        )
