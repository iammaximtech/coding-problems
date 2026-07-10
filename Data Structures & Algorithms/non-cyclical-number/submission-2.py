class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1: return False
        if n == 1: return True

        seen = set()

        while n!=1 :
            digits = [int(a) for a in str(n)]
            total = 0
            for i in digits:
                total += i*i
            if total == 1: return True
            if total in seen:
                break
            else:
                seen.add(total)
                n = total

        return False

