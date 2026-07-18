class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def backtrack(r,c,i):
            if i == len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=cols or i> len(word) or board[r][c]!= word[i] or board[r][c]=="#":
                return False
            board[r][c]="#"
            truthVal = (backtrack(r+1,c,i+1) or 
            backtrack(r-1,c,i+1) or
            backtrack(r,c+1,i+1) or
            backtrack(r,c-1,i+1))
            board[r][c]=word[i]
            return truthVal

        for i in range(rows):
            for j in range(cols):
                if backtrack(i,j,0):
                    return True
        return False