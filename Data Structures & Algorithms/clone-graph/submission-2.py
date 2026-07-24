"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        maptoNew = {}
        
        def dfs(node):
            if not node:
                return None
            if node in maptoNew:
                return maptoNew[node]
            
            copy = Node(node.val)
            maptoNew[node]=copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        return dfs(node)
        