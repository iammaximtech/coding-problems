class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True

        seen = set()

        while n!=1 :
            digits = [int(a) for a in str(n)]
            sum = 0
            for i in digits:
                sum += i*i
            if sum == 1: return True
            if sum in seen:
                break
            else:
                seen.add(sum)
                n = sum
                
        return False

