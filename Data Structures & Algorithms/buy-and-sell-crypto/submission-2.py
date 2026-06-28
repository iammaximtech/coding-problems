class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        currMin = prices[0]
        l, r = 0, 1
        ans = 0
        while l < r and r < len(prices):
            if prices[r] < currMin:
                currMin = prices[r]
                l = r
            else:
                ans = max(ans, prices[r]-currMin)
            r += 1
        return ans

