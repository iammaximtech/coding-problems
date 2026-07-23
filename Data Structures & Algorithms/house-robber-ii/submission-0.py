class Solution:
    def rob(self, nums: List[int]) -> int:
        def robhelper(i, j):
            prev1 = prev2 = 0
            for k in range(i, j+1):
                temp = max(nums[k]+prev2, prev1)
                prev2 = prev1
                prev1 = temp
            return prev1
        return max(nums[0], robhelper(0, len(nums)-2), robhelper(1, len(nums)-1))
        