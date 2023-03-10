class Solution(object):

    def __init__(self, head):
        self.head = head

    def getRandom(self):
        count = 0
        result = None
        curr = self.head

        while curr:
            count += 1
            if random.randint(1, count) == 1:
                result = curr.val
            curr = curr.next

        return result