# https://leetcode.com/problems/odd-even-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from typing import Optional

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    initial_even = even
    
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    
    odd.next = initial_even
    return head