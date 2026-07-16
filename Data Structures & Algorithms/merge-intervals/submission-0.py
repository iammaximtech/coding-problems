class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        n=len(intervals)
        ans = []
        ans.append(intervals[0])
        start, end = intervals[0][0], intervals[0][1]
        i = 1
        while i <n:
            curr = intervals[i]
            if curr[0]>end:
                ans.append(curr)
                start, end = curr[0], curr[1]
            else:
                start = ans[-1][0] = min(start,curr[0])
                end = ans[-1][1] = max(end, curr[1])
            i+=1
        return ans