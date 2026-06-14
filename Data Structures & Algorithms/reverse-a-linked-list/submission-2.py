# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = head
        prev = None

        """
        """
        while new_head is not None:
            next_node = new_head.next
            new_head.next = prev

            prev = new_head
            new_head = next_node

        # after iteration, new_head is None and prev will be pointing to head of new LL
        return prev