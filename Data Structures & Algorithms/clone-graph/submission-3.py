"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        maptoNew = {}
        dq = deque()
        maptoNew[node] = Node(node.val)
        dq.append(node)

        while dq:
            curr = dq.popleft()
            for n in curr.neighbors:
                if n not in maptoNew:
                    maptoNew[n]=Node(n.val)
                    dq.append(n)
                maptoNew[curr].neighbors.append(maptoNew[n])
        return maptoNew[node]
                    
