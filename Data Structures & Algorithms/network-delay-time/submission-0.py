class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        adj = {i:[]for i in range(n+1)}
        visited = set()
        for s,d,t in times:
            adj[s].append((d,t))
        
        heapq.heappush(heap,(0,k))
        ans = 0
        while heap:
            curr = heapq.heappop(heap)
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            ans = curr[0]
            for d, t in adj[curr[1]]:
                if d not in visited:
                    heapq.heappush(heap, (curr[0]+t,d))
        return ans if len(visited)==n else -1

        