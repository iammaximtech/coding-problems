class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l, r = 0, 0
        while r<len(nums)-1:
            furthest = nums[r]
            for i in range (l, r+1):
                furthest = max(i + nums[i],furthest)
            l = r+1
            r = furthest
            jumps+=1
        return jumps