class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to hold the merged list
        dummy = ListNode(0)
        current = dummy

        # Iterate over both lists until one of them becomes null
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Append the remaining nodes from the non-null list
        if list1:
            current.next = list1
        else:
            current.next = list2

        # Return the head of the merged list (skip the dummy node)
        return dummy.next
