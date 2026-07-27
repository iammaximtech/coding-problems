class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = collections.defaultdict(list)
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2, y2 =points[j]
                cost = abs(x1-x2)+abs(y1-y2)
                adj[i].append((cost, j))
                adj[j].append((cost, i))
        minheapMST = [(0,0)]
        visited = set()
        cost = 0
        while(len(visited)<N):
            costN, point = heapq.heappop(minheapMST)
            if point in visited:
                continue
            visited.add(point)
            cost += costN
            for c,p in adj[point]:
                if p not in visited:
                    heapq.heappush(minheapMST, (c,p))
        return cost
        