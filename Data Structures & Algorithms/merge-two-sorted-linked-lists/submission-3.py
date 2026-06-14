# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        current_node = None

        current1 = list1
        current2 = list2

        while(current1 and current2):
            val1 = current1.val
            val2 = current2.val

            if val1 < val2:
                if head is None:
                    head = current1
                    current = head
                else:
                    current.next = current1
                    current = current.next
                current1 = current1.next
            else:
                if head is None:
                    head = current2
                    current = head
                else:
                    current.next = current2
                    current = current.next
                current2 = current2.next

        while(current1):
            if head is None:
                head = current1
                current = head
            else:
                current.next = current1
                current = current.next
            current1 = current1.next

        while(current2):
            if head is None:
                head = current2
                current = head
            else:
                current.next = current2
                current = current.next
            current2 = current2.next
        return head