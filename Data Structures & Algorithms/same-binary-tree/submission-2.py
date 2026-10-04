# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Para cada nodo comparar
        def dfs(p, q):

            if p == q == None: # are igual return True
                return True

            if p is None or q is None:
                return False
            
            if p.val != q.val:
                return False

            leftSame = dfs(p.left, q.left)
            rightSame = dfs(p.right, q.right)

            return leftSame and rightSame
        
        return dfs(p, q)

        