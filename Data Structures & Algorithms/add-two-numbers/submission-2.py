# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def createLL(self, digits, length):
        head = None
        prev = None
        if len(digits) < length:
            diff = length - len(digits)
            for i in range(diff):
                digits.append(0)
        for digit in digits:
            curr = ListNode(digit, None)
            if head is None:
                head = curr
            if prev is not None:
                prev.next = curr 
            prev = curr
        if prev is not None:
            prev.next = None
        return head
    def getNumber(self, prev, length):
        number = 0
        print
        while(prev):
            number += (prev.val * pow(10, length-1))
            prev = prev.next
            length-=1
        return number
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        length1 = 0
        curr1 = l1
        prev1 = None
        while(curr1):
            next_node = curr1.next
            curr1.next = prev1
            prev1 = curr1
            curr1 = next_node
            length1 +=1

        length2 = 0
        curr2 = l2
        prev2 = None
        while(curr2):
            next_node = curr2.next
            curr2.next = prev2
            prev2 = curr2
            curr2 = next_node
            length2 +=1

        number1 = self.getNumber(prev1, length1)
        number2 = self.getNumber(prev2, length2)
        number3 = number1 + number2
        print(number3, number1, number2)
        digits = []
        while(number3 >= 1):
            digit = number3 % 10
            number3 = number3//10
            digits.append(digit)
        
        new_head = self.createLL(digits, max(length1, length2))
        return new_head