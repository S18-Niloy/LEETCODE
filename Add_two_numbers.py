# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2:
            # Get the values of the current nodes, or 0 if the nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            # Create a new node with the calculated digit
            curr.next = ListNode(digit)
            curr = curr.next

            # Move to the next nodes in the input linked lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Check if there is a remaining carry
        if carry:
            curr.next = ListNode(carry)

        return dummy.next
