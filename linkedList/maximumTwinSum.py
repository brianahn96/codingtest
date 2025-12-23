# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

def pairSum(head: Optional[ListNode]) -> int:
    max_sum = 0

    slow, fast = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    curr, prev = slow, None

    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    
    while prev:
        max_sum = max(max_sum, head.val + prev.val)
        prev = prev.next
        head = head.next

    return max_sum