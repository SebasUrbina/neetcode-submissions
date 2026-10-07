# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        [ 1 | >] -> [ 2 | >] -> [ 3 | >] -> [ 4 | >]
        next value of 4th node is pointing to two
        """ 

        seen = set()
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False

        # Optimal solution
        # slow, fast = head, head

        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        #     if slow == fast:
        #         return True
        
        # return False

        