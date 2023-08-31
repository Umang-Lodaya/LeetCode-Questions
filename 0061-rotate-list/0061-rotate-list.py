# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, node):
        if not node:
            return 0
        
        n = 0
        while node.next:
            n += 1
            node = node.next
        
        return n + 1
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head
        
        if k == 0:
            return head
        
        length = self.getLength(head)
        # print(length)
        k = k % length
        
        for _ in range(k):
            prev = None
            curr = head
            
            while curr.next:
                prev = curr
                curr = curr.next
            
            prev.next = None
            curr.next = head
            head = curr
        
        return head