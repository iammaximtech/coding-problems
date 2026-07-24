class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMax = currMin = 1
        for n in nums:
            temp = currMax
            currMax = max(currMax*n, currMin*n, n)
            currMin = min(temp*n, currMin*n, n)
            ans = max(ans, currMax)
        return ans
        