class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        currMin = prices[0]
        ans = 0
        for i in range(len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]    
            else:
                ans = max(ans, prices[i]-currMin)
        return ans

