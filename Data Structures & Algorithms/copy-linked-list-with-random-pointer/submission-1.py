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
        # deep_copy = {None:None}
        # curr = head
        # while curr:
        #     deep_copy[curr] = Node(curr.val)
        #     curr = curr.next

        # curr = head
        # while curr:
        #     copy = deep_copy[curr]
        #     copy.next = deep_copy[curr.next]
        #     copy.random = deep_copy[curr.random]

        #     curr = curr.next


        # return deep_copy[head]
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            oldToCopy[cur].val = cur.val
            oldToCopy[cur].next = oldToCopy[cur.next]
            oldToCopy[cur].random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        