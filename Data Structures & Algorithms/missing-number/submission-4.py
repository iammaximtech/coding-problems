class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n #since loop run till only n-1
        for i in range(n):
            missing ^= i ^ nums[i]
        return missing
        