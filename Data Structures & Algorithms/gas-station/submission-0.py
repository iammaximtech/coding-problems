class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:
            return -1
        prefixSumDiff = 0
        ans = 0
        for i in range(len(gas)):
            prefixSumDiff += gas[i]-cost[i]
            if prefixSumDiff <0:
                prefixSumDiff = 0
                ans = i+1
        return ans