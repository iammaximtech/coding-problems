class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        adj = {i:set() for i in range(n)}
        for e in edges:
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        visited = set()
        count =0
        def dfs(i):
            if i in visited:
                return 
            visited.add(i)
            for j in adj[i]:
                dfs(j)
        for i in range(n):
            if i not in visited:
                dfs(i)
                count+=1
            if len(visited)==n:
                break
        return count
                
        
        
