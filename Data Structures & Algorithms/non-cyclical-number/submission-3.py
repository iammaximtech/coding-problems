class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True

        def getSquaredSum(n):
            total = 0
            while n>0:
                digit = n%10
                total += digit*digit
                n = n//10
            return total

        seen = set()
        
        while n!=1 :
            total = getSquaredSum(n)
            if total == 1: return True
            if total in seen:
                break
            else:
                seen.add(total)
                n = total

        return False

