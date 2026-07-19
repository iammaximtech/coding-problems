class Solution:
    def jump(self, nums: List[int]) -> int:
        minjumps = 0
        l = r = 0
        while r<len(nums)-1:
            furthest = nums[r]
            for i in range (l, r+1):
                furthest = max(nums[i]+ i, furthest)
            minjumps += 1
            l = r+1
            r= furthest
        return minjumps
