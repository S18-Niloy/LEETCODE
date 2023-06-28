class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k):
        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Find the kth node from the beginning
        kth_node_from_beginning = None
        current = head
        for _ in range(k - 1):
            current = current.next
        kth_node_from_beginning = current
        
        # Find the kth node from the end
        kth_node_from_end = None
        current = head
        for _ in range(length - k):
            current = current.next
        kth_node_from_end = current
        
        # Swap the values of the kth nodes
        kth_node_from_beginning.val, kth_node_from_end.val = kth_node_from_end.val, kth_node_from_beginning.val
        
        # Return the head of the updated linked list
        return head

# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create an instance of Solution
solution = Solution()

# Swap the values of the 2nd node from the beginning and the 2nd node from the end
k = 2
new_head = solution.swapNodes(head, k)

# Traverse the updated linked list and print the values
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next

