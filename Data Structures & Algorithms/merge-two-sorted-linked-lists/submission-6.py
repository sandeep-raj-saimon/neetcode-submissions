# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        curr1 = list1
        curr2 = list2
        head = None
        curr = None
        while (curr1 is not None and curr2 is not None):
            curr1_val = curr1.val
            curr2_val = curr2.val
            # print(curr1_val, curr2_val)
            if curr1_val < curr2_val:
                # print(curr1_val)
                if head is None:
                    head = curr1
                    curr = curr1
                else:
                    curr.next = curr1
                    curr = curr.next
                curr1 = curr1.next
            else:
                # print(curr2_val)
                if head is None:
                    head = curr2
                    curr = curr2
                else:
                    curr.next = curr2
                    curr = curr.next
                curr2 = curr2.next

        while curr1 is not None:
            # print("in curr1")
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next

        while curr2 is not None:
            # print("in curr2")
            curr.next = curr2
            curr2 = curr2.next
            curr = curr.next

        return head