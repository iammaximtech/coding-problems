class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        nodes = {i:[] for i in range(n)}
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])
        visited = set()
        def dfs(i,prev):
            if i in visited:
                return False
            visited.add(i)
            for j in nodes[i]:
                if j == prev:
                    continue
                if not dfs(j,i):
                        return False
            return True
                
        
        return dfs(0,-1) and len(visited)==n
