# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        double = single = head
        while double and double.next != None:
            single = single.next
            double = double.next.next
            if single == double:
                return True
        return False