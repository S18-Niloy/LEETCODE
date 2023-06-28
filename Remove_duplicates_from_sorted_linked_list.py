class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Handle edge case of an empty linked list
        if not head:
            return None
        
        # Set the current pointer to the head
        current = head
        
        # Traverse the linked list and remove duplicates
        while current.next:
            # If the current node's value is equal to the next node's value, skip the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the head of the updated linked list
        return head
