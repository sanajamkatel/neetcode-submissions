# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head:
        #     return 

        # nodes = []
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # i = 0 
        # j = len(nodes) - 1
        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1

        #     if i >= j:
        #         break

        #     nodes[j].next = nodes[i]
        #     j -= 1

        # nodes[i].next = None

        slow = head 
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next 
        prev = slow.next = None

        while second:
            temp_next = second.next
            second.next = prev
            prev = second
            second = temp_next

        first = head 
        second = prev

        while second:
            tmp1 , tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 
            first, second = tmp1, tmp2

                
            


        




        