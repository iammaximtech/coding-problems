class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1]*n
        
        def findRoot(i):
            curr = i
            while curr != parents[curr]:
                parents[curr]= parents[parents[curr]]
                curr = parents[curr]
            return curr
        
        def unionRoots(v1, v2):
            r1 = findRoot(v1)
            r2 = findRoot(v2)
            if r1 == r2:
                return 0
            if rank[r2]>rank[r1]: 
                r2, r1 = r1, r2 #swap so dont have copy logic and use r1 as bigger rank next
            parents[r2] = parents[r1]
            rank[r1]+=rank[r2]
            return 1
        groups = n
        for e1, e2 in edges:
            groups-= unionRoots(e1, e2)
        return groups

