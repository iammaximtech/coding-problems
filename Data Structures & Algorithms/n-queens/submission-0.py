class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        curr = [["."]*n for _ in range(n)]
        bookedRow = set()
        bookedCol = set()
        bookedPosDiag = set() # up to down r-c=0
        bookedNegDiag = set() # down to upr+c=0

        def backtracking(r):
            if r == n:
                ans.append(["".join(row.copy()) for row in curr])
                return
            for c in range(n):
                if c in bookedCol or r+c in bookedPosDiag or r-c in bookedNegDiag:
                    continue
                curr[r][c]="Q"
                bookedCol.add(c)
                bookedPosDiag.add(r+c)
                bookedNegDiag.add(r-c)
                backtracking(r+1)
                curr[r][c]="."
                bookedCol.remove(c)
                bookedPosDiag.remove(r+c)
                bookedNegDiag.remove(r-c)
                
        backtracking(0)
        return ans


        