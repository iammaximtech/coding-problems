class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) -1
        while l < r:
            curr = nums[l]+nums[r]
            if curr < target:
                l += 1
            elif curr > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []

            
