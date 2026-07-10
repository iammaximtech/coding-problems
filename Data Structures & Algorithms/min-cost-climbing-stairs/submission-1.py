class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0
        if len(cost)==1: return cost[0]
        if len(cost)==2: return min(cost[0],cost[1])
        prev, curr = cost[0], cost[1]
        n = len(cost)
        for i in range(2,n):
            new = min(prev,curr)+cost[i]
            prev, curr =curr ,new
        return min(prev,curr)
