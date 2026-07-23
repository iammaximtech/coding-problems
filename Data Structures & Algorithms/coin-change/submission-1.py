class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+10]*(amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for n in coins:
                if i>=n:
                    dp[i] = min(dp[i], dp[i-n]+ 1) #1 == dp[n] 1 since one coin needed
        return dp[amount] if dp[amount]!=amount+10 else -1