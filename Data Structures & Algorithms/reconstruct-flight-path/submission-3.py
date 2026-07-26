class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = {i:[] for i,_ in tickets}
        for s, d in tickets:
            adj[s].append(d)
        ans = ["JFK"]

        def dfsbacktrack(city): #eulerian algo
            if len(ans)==len(tickets)+1: #eulerian always visits all edges, +1 for adding jfk
                return True
            if city not in adj:
                return False
            temp = adj[city].copy()
            for i,v in enumerate(temp): #to maintain order need both index and value to pop back in right place
                ans.append(v)
                adj[city].pop(i)
                if dfsbacktrack(v):
                    return True
                ans.pop()
                adj[city].insert(i,v)
            return False
            
        
        dfsbacktrack("JFK")
        return ans