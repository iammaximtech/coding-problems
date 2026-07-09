class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        l = 0
        r = len(nums)-1
        while l<=r and -1<l<len(nums) and -1<r<len(nums):
            mid = (r+l)//2
            if target == nums[mid]:
                ans = mid
                break
            elif target<nums[mid]:
                r = mid -1
            else:
                l = mid + 1
        return ans      