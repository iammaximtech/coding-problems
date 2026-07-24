class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        currMax = currMin = 1
        for n in nums:
            if n==0:
                currMax = currMin = 1
            temp = currMax
            currMax = max(currMax*n, currMin*n, n)
            currMin = min(temp*n, currMin*n, n)
            ans = max(ans, currMax)
        return ans
        