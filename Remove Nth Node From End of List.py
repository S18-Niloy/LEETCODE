class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both slow and fast pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node by adjusting the pointers
        slow.next = slow.next.next
        
        # Return the updated head of the list
        return dummy.next

# Create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Create an instance of Solution
solution = Solution()

# Remove the 2nd node from the end of the list
n = 2
new_head = solution.removeNthFromEnd(head, n)

# Traverse the updated linked list and print the values
current = new_head
while current:
    print(current.val, end=" -> ")
    current = current.next
