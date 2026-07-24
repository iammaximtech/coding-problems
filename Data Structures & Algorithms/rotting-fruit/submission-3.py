class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dq = collections.deque()
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    dq.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        minutes = 0
        while dq and fresh>0:
            length = len(dq)
            minutes += 1
            for i in range(length):
                curr = dq.popleft()
                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                for row, col in neighbors:
                    r = curr[0]+row
                    c = curr[1]+col
                    if r>=0 and c>=0 and r<ROWS and c<COLS and grid[r][c]==1:
                        grid[r][c]=2
                        fresh -= 1
                        dq.append((r,c))
        return minutes if fresh ==0 else -1