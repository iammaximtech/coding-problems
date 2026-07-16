class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or len(points) < k: return []
        h = []
        for point in points:
            heapq.heappush(h,(-(point[0]**2+point[1]**2), point))
            if len(h)>k:
                heapq.heappop(h)
        ans = []
        for a,b in h:
            ans.append(b)
        return ans 
        
        