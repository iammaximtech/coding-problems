class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or len(points) < k: return []
        h = []
        for point in points:
            h.append((-(point[0]**2+point[1]**2), point))
        heapq.heapify(h)
        while len(h)>k:
            heapq.heappop(h)
        ans = [i[1] for i in h]
        return ans 
        
        