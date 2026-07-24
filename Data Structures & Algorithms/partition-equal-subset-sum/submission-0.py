class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numSum = sum(nums)
        if numSum%2==1:
            return False
        target = numSum//2
        dp = set()
        for n in nums:
            nextDp = dp.copy()
            for s in dp:
                nextDp.add(s+n)
                if target in nextDp:
                    return True
            nextDp.add(n)
            dp = nextDp
        return True if target in dp else False

        