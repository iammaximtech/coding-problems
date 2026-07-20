class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        lastEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if lastEnd<=start:
                lastEnd = end
            else:
                ans += 1
                lastEnd = min(lastEnd, end)
        return ans