class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        ans =1
        length = len(nums)
        for i in s:
            nxt = i+1
            prev = i-1
            front = 1
            while nxt in s and prev not in s:
                nxt += 1
                front += 1
                if front > ans:
                    ans = front
        return ans
                




