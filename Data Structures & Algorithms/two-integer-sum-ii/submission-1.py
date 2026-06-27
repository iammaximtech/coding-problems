class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        while l < r and r < len(nums):
            while (r < len(nums) and 
            (nums[l] + nums[r]) < target):
                r +=1 
            if r < len(nums) and (nums[l] + nums[r]) == target:
                return [l+1, r+1]
            l += 1
            r = l +1
        return []

            
