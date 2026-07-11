class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        n = len(nums)
        for i in range(n):
            missing ^= i
            missing ^= nums[i]
        missing ^= n
        return missing
        