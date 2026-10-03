# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # if not root:
        #     return 0
        
        # k = max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return 1 + k
        # dfs iterative

        # stack = [[root, 1]]
        # res = 0
        # while stack:
        #     node, depth = stack.pop(-1)

        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left, depth + 1])
        #         stack.append([node.right, depth + 1])


        # Bfs by nivel
        if not root:
            return 0

        queue = [root]
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
