# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev = None
        while(current_node):
            next_node = current_node.next
            if current_node == head:
                current_node.next = None
            else:
                current_node.next = prev
            prev = current_node
            current_node = next_node
        return prev