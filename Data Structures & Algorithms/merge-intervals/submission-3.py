class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        n=len(intervals)
        ans = []
        ans.append(intervals[0])
        i = 1
        while i <n:
            curr = intervals[i]
            last = ans[-1]
            if curr[0]>last[1]:
                ans.append(curr)
            else:
                last[0] = min(last[0],curr[0])
                last[1] = max(last[1], curr[1])
            i+=1
        return ans