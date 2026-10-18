# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0   1   2   3   4   5
       [0, n-1, 1, n-2, 2, n-3, ...]
        i                    j
        i, j, i+1, j-1, i+1    

        1 -> 2 -> 3 -> 4 -> 5 -> None
        1 -> 5 -> 2 -> 4
        """
        # Brute force approach
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        i, j = 0, len(nodes) - 1

        while i < j:

            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None

        

        # first = head
        # prev = None
        # last = head

        # while first:
        #     while last.next: 
        #         prev = last
        #         last = last.next
            
        #     nextNode = first.next # -> 2
        #     prev.next = None 
        #     first.next = last # 1 -> 5
        #     last.next =   # 5 -> 2
        #     first = nextNode # -> 2
            



        