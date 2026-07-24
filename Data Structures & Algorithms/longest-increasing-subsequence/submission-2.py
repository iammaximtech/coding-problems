from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for n in nums:
            if n>dp[-1]:
                dp.append(n)
            else:
                i = bisect_left(dp, n)
                dp[i] = n
        return len(dp)