class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums: return -1
        n = len(nums)
        for num in nums:
            i = abs(num)
            if nums[i-1]<0: 
                return i
            nums[i-1]*= -1
        return -1
        