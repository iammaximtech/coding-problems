class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            diff = abs(heapq.heappop(maxheap))-abs(heapq.heappop(maxheap))
            if diff > 0:
                heapq.heappush(maxheap,-diff)
        return -maxheap[0] if maxheap else 0