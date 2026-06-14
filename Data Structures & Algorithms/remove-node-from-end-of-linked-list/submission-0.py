# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        if n == 0:
            return head
        length = 0
        current_node = head

        while(current_node):
            current_node = current_node.next
            length += 1
    
        index = 0
        current_node = head
        while(current_node and index < length - n - 1):
            current_node = current_node.next
            index +=1
            print(index)


        if n == length: # remove head node:
            if current_node.next:
                head = current_node.next
            else:
                head = None
        elif n < length:
            if current_node.next:
                current_node.next = current_node.next.next
            else:
                current_node.next = None
        else:
            pass
        return head