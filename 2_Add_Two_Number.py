# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0 #初始化进位
        dummyHead = ListNode(0)
        curr = dummyHead
        
        while(l1 or l2):
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(1)
        return dummyHead.next
            
l1 = ListNode(2)       
l1 = l1.next
l1 = ListNode(4)

        
        
        
        
