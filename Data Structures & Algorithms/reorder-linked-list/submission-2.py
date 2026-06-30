# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we will use slow and fast pointer for finding
        # the mid point of LL

        slow = head
        fast = head.next
        if fast is None:
            return
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow points to the middle of LL
        head2 = slow.next
        slow.next = None
        # now we need to reverse the LL whose head is head2
        prev = None
        while head2 is not None:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp

        first, second = head, prev

        while first and second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2