# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head will keep track of the newly created LL, and current_node will keep track of current node of newly created LL.
        head = None
        current_node = None
        current_node1 = list1
        current_node2 = list2

        while (current_node1 and current_node2):
            val1 = current_node1.val
            val2 = current_node2.val

            if val1 < val2:
                # there can be 2 cases, head is None and head is not None
                if head == None:
                    head = current_node1
                    current_node = head
                else:
                    current_node.next = current_node1
                    current_node = current_node.next
                current_node1  = current_node1.next
            else:
                if head == None:
                    head = current_node2
                    current_node = head
                else:
                    current_node.next = current_node2
                    current_node = current_node.next
                current_node2  = current_node2.next

            # we need to all looks for cases where one LL is greater than other LL
        while(current_node1):
            if head == None:
                head = current_node1
                current_node = head
            else:
                current_node.next = current_node1
                current_node = current_node.next
            current_node1  = current_node1.next
        
        while(current_node2):
            if head == None:
                head = current_node2
                current_node = head
            else:
                current_node.next = current_node2
                current_node = current_node.next
            current_node2  = current_node2.next
        return head