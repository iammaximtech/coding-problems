class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r,c, letter):
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]=="X" or board[r][c]=="T":
                return 
            board[r][c]=letter
            dfs(r+1,c, letter)
            dfs(r-1,c, letter)
            dfs(r,c+1, letter)
            dfs(r,c-1, letter)
        for r in range(ROWS):
            dfs(r, 0, "T")
            dfs(r, COLS-1, "T")
        for c in range(COLS):
            dfs(0, c, "T")
            dfs(ROWS-1, c, "T")
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
                elif board[r][c]=="T":
                    board[r][c]="O"
        
        
        