class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dq = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    dq.append((r,c,0))
        minutes = 0
        while dq:
            length = len(dq)
            for i in range(length):
                curr = dq.popleft()
                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                for row, col in neighbors:
                    r = curr[0]+row
                    c = curr[1]+col
                    t = curr[2]+1
                    if r>=0 and c>=0 and r<ROWS and c<COLS and grid[r][c]==1:
                        grid[r][c]=2
                        dq.append((r,c,t))
                        minutes = t
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return minutes 