# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:

    if not head or not head.next:
        return

    slow = head
    fast = head.next

    while fast and fast.next:
        if fast.next.next:
            slow = slow.next
        fast = fast.next.next
    
    if slow.next:
        slow.next = slow.next.next

    return head