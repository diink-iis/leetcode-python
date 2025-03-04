# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True
