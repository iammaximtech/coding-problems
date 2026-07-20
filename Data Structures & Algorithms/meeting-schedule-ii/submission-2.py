"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        minheap = []
        heapq.heapify(minheap)
        ans = 0
        for i in intervals:
            if minheap and minheap[0] <= i.start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)
            ans = max(ans,len(minheap))
        return ans