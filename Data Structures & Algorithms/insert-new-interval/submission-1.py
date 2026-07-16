class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        start = newInterval[0]
        end = newInterval[1]

        i = 0
        while i<n and intervals[i][1]<start:
            ans.append(intervals[i])
            i+=1
        
        while i<n and intervals[i][0]<=end:
            start = min(start,intervals[i][0])
            end = max(end, intervals[i][1])
            i+=1
        ans.append([start,end])
        for i in range(i, n):
            ans.append(intervals[i])
        return ans