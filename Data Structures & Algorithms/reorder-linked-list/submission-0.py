# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        current = slow.next
        slow.next = prev = None

        while(current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        first, second = head, prev
        count = 0
        while(first and second):
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        

        