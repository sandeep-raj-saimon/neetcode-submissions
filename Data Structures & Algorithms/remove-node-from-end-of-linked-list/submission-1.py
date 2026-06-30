# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, head):
        prev = None
        while head is not None:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse the LL
        head = self.reverseLL(head)
        count = 1
        first = None
        second = head
        while second is not None:
            if count == n:
                break
            
            first = second
            second = second.next
            count+=1

        if second and first:
            first.next = second.next
        elif second and not first:
            head = second.next
        else:
            pass
            
        head = self.reverseLL(head)
        return head
            
