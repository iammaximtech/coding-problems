class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3: return n
        recent = [1,2]
        for i in range(3,n+1):
            first = recent[0]
            second = recent[1]
            recent[0]=second
            recent[1]=first+second
        return recent[1]
