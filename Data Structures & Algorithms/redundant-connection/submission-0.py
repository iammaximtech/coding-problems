class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)] #add extra as nodes are 1 indexed so they still point to themselves
        rank = [1]*(n+1) #same reason

        def find(i):
            curr = i
            while curr != parent[curr]:
                parent[curr]= parent[parent[curr]]
                curr = parent[curr]
            return curr
        
        def union(i, j):
            p1, p2 = find(i), find(j)
            if p1 == p2:
                return False
            if rank[p2] > rank[p1]:
                p2, p1 = p1, p2 #swap to avoid duplicate logic and consider p1 rank as higher
            parent[p2] = parent[p1]
            rank[p1]+=rank[p2]
            return True
        
        for i in range(n): #dont reverse loop as there's only edge that will break and it should be the last one
            if not union(edges[i][0],edges[i][1]):
                return edges[i]
        return []