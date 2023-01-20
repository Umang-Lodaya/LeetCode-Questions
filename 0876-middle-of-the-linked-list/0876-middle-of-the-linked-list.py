# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        n = 0
        while head.next:
            head = head.next
            n += 1
        n += 1
        
        n = n//2 + 1
        
        while n-1:
            current = current.next
            n -= 1
        
        return current