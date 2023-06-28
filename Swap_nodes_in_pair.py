class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Set the current and prev pointers
        prev = dummy
        current = head
        
        # Traverse the linked list and swap pairs of adjacent nodes
        while current and current.next:
            # Nodes to be swapped
            first_node = current
            second_node = current.next
            
            # Swap the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Update the pointers for the next iteration
            prev = first_node
            current = first_node.next
        
        # Return the head of the updated linked list
        return dummy.next
