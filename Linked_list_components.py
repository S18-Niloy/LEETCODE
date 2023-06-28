class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head, nums):
        # Create a set of the values in nums for efficient lookup
        num_set = set(nums)
        
        # Initialize variables
        component_count = 0
        is_connected = False
        
        # Traverse the linked list
        current = head
        while current:
            # Check if the current node's value is in nums
            if current.val in num_set:
                # If not connected to a component, start a new component
                if not is_connected:
                    component_count += 1
                is_connected = True
            else:
                is_connected = False
            current = current.next
        
        # Return the number of connected components
        return component_count
