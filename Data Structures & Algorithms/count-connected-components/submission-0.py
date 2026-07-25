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
        def dfs(i,prev):
            if i in visited:
                return 
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                dfs(j,i)
        for i in range(n):
            if i not in visited:
                dfs(i,i-1)
                count+=1
            if count==n:
                break
        return count
                
        
        
