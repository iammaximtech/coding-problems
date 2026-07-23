class Solution:
    def rob(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i-2>= 0:
                nums[i] = max(nums[i]+nums[i-2], nums[i-1])
            elif i-1>=0:
                nums[i] = max(nums[i], nums[i-1])
        return nums[len(nums)-1]
        