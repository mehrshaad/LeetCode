# LeetCode
# Problem: Remove Duplicates from Sorted List
# Difficulty: Easy
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution class for the problem
class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        curr = head
        while curr:
            if tail == dummy or tail.val != curr.val:
                tail.next = ListNode(curr.val)
                tail = tail.next
            curr = curr.next
        return dummy.next
