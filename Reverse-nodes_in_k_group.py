# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Helper function to reverse a sublist of size k
        def reverseSublist(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, curr

        # Check if there are at least k nodes remaining
        count = 0
        node = head
        while count < k and node:
            node = node.next
            count += 1

        # Reverse the current group if there are k nodes
        if count == k:
            reversed_head, reversed_tail = reverseSublist(head, k)
            head.next = self.reverseKGroup(reversed_tail, k)
            return reversed_head

        # Return the remaining nodes as is
        return head
