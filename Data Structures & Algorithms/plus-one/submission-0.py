class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        carry = 1
        mul = 1
        for i in range(len(digits)-1,-1,-1):
            number += digits[i] * mul 
            mul *= 10
        number += 1
        ans = []
        divBy = 10** (len(str(number))-1)
        totalDigits = len(str(number))
        while totalDigits > 0:
            digit = number//divBy
            ans.append(digit)
            number = number - (digit*divBy)
            divBy = divBy//10
            totalDigits -= 1
        return ans