class Solution:
    def isHappy(self, n: int) -> bool:
        if n<1: return False
        if n==1: return True

        def nextNumber(n):
            total = 0
            while n>0:
                digit = n%10
                total+= digit*digit
                n = n//10
            return total
        
        slow, fast = n, nextNumber(n)
        while slow != fast:
            slow = nextNumber(slow)
            fast = nextNumber(fast)
            fast = nextNumber(fast)
        return fast == 1
        