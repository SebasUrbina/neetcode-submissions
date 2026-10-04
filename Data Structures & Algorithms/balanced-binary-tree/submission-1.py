# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # heightDiff = leftHeight - rightHeight
        # Por cada root calcula leftHeight and rightHeight

        leftHeight = 0
        rightHeight = 0
        def dfs(root):

            if not root:
                return (True, 0)
            
            leftBalanced, leftHeight = dfs(root.left)
            rightBalanced, rightHeight = dfs(root.right)

            balanced = leftBalanced and rightBalanced and (abs(rightHeight - leftHeight) <= 1)
            height = 1 + max(leftHeight, rightHeight)


            return (balanced, height)
        balanced, height = dfs(root)

        return balanced

        