class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ones = 0
            n = i
            while n>0:
                n = n & (n-1)
                ones += 1
            ans[i] = ones
        return ans
        