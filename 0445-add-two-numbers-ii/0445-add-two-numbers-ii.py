class Solution:
    def addTwoNumbers(self, l1, l2):
        stack1, stack2 = [], []

        # Push values of l1 into stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next

        # Push values of l2 into stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        result = None

        while stack1 or stack2 or carry:
            sum_val = carry

            # Add the top values from stack1 and stack2, if available
            if stack1:
                sum_val += stack1.pop()
            if stack2:
                sum_val += stack2.pop()

            # Create a new node with the sum % 10
            node = ListNode(sum_val % 10)

            # Set the new node as the next node of the result list
            node.next = result
            result = node

            # Update the carry
            carry = sum_val // 10

        return result