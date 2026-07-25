class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        reachAtl, reachPac = set(), set()

        def dfs(r,c,canReach,prevH):
            if r<0 or c<0 or r==ROWS or c==COLS or heights[r][c]<prevH or (r,c) in canReach:
                return
            canReach.add((r,c))
            neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
            for nr, nc in neighbors:
                dfs(r+nr,c+nc,canReach,heights[r][c])

        for c in range(COLS):
            dfs(0,c,reachPac, heights[0][c])
            dfs(ROWS-1,c,reachAtl, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r,0,reachPac, heights[r][0])
            dfs(r,COLS-1,reachAtl, heights[r][COLS-1])
        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in reachAtl and (r,c) in reachPac:
                    ans.append([r,c])
        return ans