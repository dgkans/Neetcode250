# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next #temp is for iterating through the nodes
            curr.next = prev #reverse the link
            prev = curr #update previous node
            curr = temp #update curr to next node in link
        return prev
