class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        chars = {}
        chars["2"]="abc"
        chars["3"]="def"
        chars["4"]="ghi"
        chars["5"]="jkl"
        chars["6"]="mno"
        chars["7"]="pqrs"
        chars["8"]="tuv"
        chars["9"]="wxyz"

        ans =[]
        curr =[]

        def backtrackdfs(i):
            if i==len(digits):
                ans.append("".join(curr.copy()))
                return 
            for c in chars[digits[i]]:
                curr.append(c)
                backtrackdfs(i+1)
                curr.pop()
        backtrackdfs(0)
        return ans
