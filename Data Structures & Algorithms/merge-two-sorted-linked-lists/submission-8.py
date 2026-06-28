# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2

        if list1 is None:
            return list2

        if list2 is None:
            return list1

        new_head = None
        curr = None
        while head1 is not None and head2 is not None:
            curr1_val = head1.val
            curr2_val = head2.val

            if curr1_val < curr2_val:
                if new_head is None:
                    new_head = head1
                    curr = head1
                else:
                    curr.next = head1
                    curr = curr.next
                
                head1 = head1.next
            else:
                if new_head is None:
                    new_head = head2
                    curr = head2
                else:
                    curr.next = head2
                    curr = curr.next
                
                head2 = head2.next

        while head1 is not None:
            curr.next = head1
            head1 = head1.next
            curr = curr.next

        while head2 is not None:
            curr.next = head2
            head2 = head2.next
            curr = curr.next

        return new_head

