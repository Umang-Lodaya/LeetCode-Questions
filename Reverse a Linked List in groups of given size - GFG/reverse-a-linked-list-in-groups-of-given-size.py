"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head):
        s = 0
        while head:
            head = head.next
            s += 1
        
        return s
        
    def reverse(self,head, k):
        size = self.count(head)
        
        if size == 0 or head == None:
            return None
        
        curr = head
        
        prev = None
        
        t = 0
        
        if size < k:
            k = size
        
        while t < k:
            curr = curr.next
            head.next = prev
            prev = head
            head = curr
            t += 1
            
        now = prev
        
        while prev.next is not None:
            prev = prev.next
            
        prev.next = self.reverse(curr, k)
        return now


#{ 
 # Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()

if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob=Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1




# } Driver Code Ends