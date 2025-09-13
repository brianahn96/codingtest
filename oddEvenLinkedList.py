# https://leetcode.com/problems/odd-even-linked-list/

def oddEvenList(head):
    if not head:
        return head
    
    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next
    
    odd.next = even_head
    return head