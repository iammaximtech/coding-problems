class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        nodes = {i:[] for i in range(n)}
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])
        visited = set()
        def bfs(i):
            dq =collections.deque()
            dq.append(i)
            visited.add(i)
            while dq:
                curr = dq.popleft()
                for c in nodes[curr]:
                    if c not in visited:
                        dq.append(c)
                        visited.add(c)
        bfs(0)
        return len(visited)==n
