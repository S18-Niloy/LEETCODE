class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        # Handle edge cases of an empty list or a list with only one node
        if not head or not head.next:
            return head
        
        # Initialize pointers for odd and even nodes
        odd = head
        even = head.next
        
        # Save the head of the even list to connect it later
        even_head = even
        
        # Rearrange the list by connecting odd nodes and even nodes separately
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # Connect the odd list and the even list
        odd.next = even_head
        
        # Return the head of the reordered list
        return head
