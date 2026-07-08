import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i+1 >= k:
                while heap[0][1] < i-k+1:
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans


        
                

