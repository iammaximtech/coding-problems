class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = collections.defaultdict(list)
        for s, d in tickets[::-1]:
            adj[s].append(d)
        ans = []

        def dfsEulerian(city): #eulerian algo
            while adj[city]:
                next = adj[city].pop()
                dfsEulerian(next)
            ans.append(city)
            
        
        dfsEulerian("JFK")
        return ans[::-1]