"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        # create new nodes    
        curr = head
        while curr:
           new_node = Node(curr.val)
           new_node.next = curr.next
           curr.next = new_node
           curr = new_node.next
        
        #copy random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        #separate the two lists:
        curr = head
        newhead = head.next
        newcurr = newhead
        while curr:
            curr.next = newcurr.next
            curr = curr.next
            if curr:
                newcurr.next = curr.next
                newcurr = newcurr.next
        return newhead
        
