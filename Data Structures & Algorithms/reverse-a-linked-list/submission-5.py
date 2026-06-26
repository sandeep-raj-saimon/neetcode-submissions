# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while (head is not None):
            temp = head.next # for storing the next node
            head.next = prev # for reversing the pointer
            # if head.next and head.next.next:
            #     print("next val", head.val, head.next.val, head.next.next.val)
            prev = head # for maintaining the chain
            head = temp # this is moving forward

        return prev