class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        # Handle edge cases of an empty list or when k is 0
        if not head or k == 0:
            return head
        
        # Find the length of the linked list
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        # Calculate the actual rotation index
        k %= length
        
        # Handle cases when k is a multiple of the list length
        if k == 0:
            return head
        
        # Find the new tail and the new head of the rotated list
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # Break the list to rotate
        new_tail.next = None
        
        # Find the end of the original list and connect it to the head
        current = new_head
        while current.next:
            current = current.next
        current.next = head
        
        # Return the head of the rotated list
        return new_head
