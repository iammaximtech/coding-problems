class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n*(n+1)//2
        curr = 0
        for i in nums:
            curr += i
        return total - curr
        