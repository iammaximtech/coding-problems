class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            left = abs(heapq.heappop(maxheap))-abs(heapq.heappop(maxheap))
            if left > 0:
                heapq.heappush(maxheap,-left)
        return abs(maxheap[0]) if len(maxheap)==1 else 0