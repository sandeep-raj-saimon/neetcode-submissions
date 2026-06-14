# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        while(first):
            if first.val == "":
                return True
            first.val = ""
            first = first.next
        return False
        