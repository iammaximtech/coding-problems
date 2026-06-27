class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        ans =1
        length = len(nums)
        for i in s:
            if i-1 not in s:
                nxt = i+1
                curr = 1
                while nxt in s:
                    nxt += 1
                    curr += 1
                    ans = max(ans, curr)
        return ans
                




