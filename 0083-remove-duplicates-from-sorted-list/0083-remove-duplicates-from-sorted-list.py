# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        unique = list()
        while head:
            if head.val not in unique: unique.append(head.val)
            head = head.next
            
        head = ListNode()
        start = head
        
        prev = ListNode()
        prev.next = head
        
        for i in range(len(unique)):
            head.val = unique[i]
            head.next = ListNode()
            head = head.next
            prev = prev.next
        
        prev.next = None        
        return start