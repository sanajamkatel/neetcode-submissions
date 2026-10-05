# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # brute force
        # nodes = []

        # for lst in lists:
        #     while lst:
        #         nodes.append(lst.val)
        #         lst = lst.next

        # nodes.sort()

        # res = ListNode(0)
        # curr = res
        # for node in nodes:
        #     curr.next = ListNode(node)
        #     curr = curr.next

        # return res.next

        heap = []

        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i , node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i , node.next))

        return dummy.next




        