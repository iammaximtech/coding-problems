class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        recent = [1,2]
        for i in range(3,n+1):
            first = recent[0]
            second = recent[1]
            recent[0]=second
            recent[1]=first+second
        return recent[1]
