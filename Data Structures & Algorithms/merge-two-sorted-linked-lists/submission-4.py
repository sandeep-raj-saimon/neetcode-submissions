# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        current1= list1
        current2= list2

        current = None

        # new_head is the head of merged LL and current is pointing to newly added LLN.
        while(current1 and current2):
            val1 = current1.val
            val2 = current2.val

            if val1 < val2:
                if new_head is None:
                    new_head = current1
                    current = current1
                else:
                    # head is not None, we need to set current
                    current.next = current1
                    current = current1
                current1 = current1.next
            else:
                if new_head is None:
                    new_head = current2
                    current = current2
                else:
                    # head is not None, we need to set current
                    current.next = current2
                    current = current2
                current2 = current2.next
        
        # if any of LL is longer than other one
        while(current1):
            if new_head is None:
                new_head = current1
                current = current1
            else:
                # head is not None, we need to set current
                current.next = current1
                current = current1
            current1 = current1.next

        while(current2):
            if new_head is None:
                new_head = current2
                current = current2
            else:
                # head is not None, we need to set current
                current.next = current2
                current = current2
            current2 = current2.next

        return new_head