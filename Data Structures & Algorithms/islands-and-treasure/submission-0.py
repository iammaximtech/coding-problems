class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dq = collections.deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]== 0:
                    dq.append((r,c))
                    visited.add((r,c))
        distance =0
        while dq:
            length = len(dq)
            for i in range(length):
                curr = dq.popleft()
                neighbors = [(0,1), (0,-1), (1,0), (-1,0)]
                for r,c in neighbors:
                    row = curr[0]+r
                    col = curr[1]+c
                    if (row>=0 and col >=0 and row<ROWS and 
                    col<COLS and grid[row][col]!=-1 and (row,col) not in visited):
                        dq.append((row,col))
                        visited.add((row,col))
                        grid[row][col] = distance +1
            distance += 1
        