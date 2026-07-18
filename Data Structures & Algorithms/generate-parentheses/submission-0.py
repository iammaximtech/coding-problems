class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []

        def backtracking(openP, closeP):
            if openP == closeP == n:
                ans.append("".join(stack))
                return
            if openP<n:
                stack.append("(")
                backtracking(openP+1,closeP)
                stack.pop()
            if closeP<openP:
                stack.append(")")
                backtracking(openP,closeP+1)
                stack.pop()
        backtracking(0,0)
        return ans