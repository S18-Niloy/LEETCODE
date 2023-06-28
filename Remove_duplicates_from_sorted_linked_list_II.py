class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Set the prev and current pointers
        prev = dummy
        current = head
        
        # Traverse the linked list and remove nodes with duplicate values
        while current:
            # Check if the current node has duplicates
            if current.next and current.val == current.next.val:
                # Move the current pointer until a distinct value is found
                while current.next and current.val == current.next.val:
                    current = current.next
                # Skip all the nodes with duplicate values
                prev.next = current.next
            else:
                # Move to the next node
                prev = prev.next
            current = current.next
        
        # Return the head of the updated linked list
        return dummy.next
