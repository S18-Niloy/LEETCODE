class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head, k):
        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the size of each part and the number of larger parts
        part_size = length // k
        extra_parts = length % k
        
        # Create an array to store the result parts
        result = [None] * k
        
        # Split the linked list into parts
        current = head
        for i in range(k):
            result[i] = current
            # Determine the size of the current part
            size = part_size + (1 if extra_parts > 0 else 0)
            extra_parts -= 1
            
            # Move to the end of the current part
            for j in range(size - 1):
                if current:
                    current = current.next
            # Break the link to the next part
            if current:
                temp = current.next
                current.next = None
                current = temp
        
        # Return the array of parts
        return result
