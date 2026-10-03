"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # adjList = [
        #     [2], # Node 1 -> 2
        #     [1,3], # Node 2 -> 1 & 3
        #     [2] # Node 3 -> 2
        # ]

        oldToNew = {} # {node: copy}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
            
        return dfs(node) if node else None

                

                
