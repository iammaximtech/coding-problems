class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = 0
        rows =len(grid)
        cols =len(grid[0])
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            area = 0
            while q:   
                row, col = q.popleft()
                area += 1
                neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                for nr, nc in neighbors:
                    if (row+nr>=0 and row+nr<rows and col+nc>=0 and col+nc<cols and
                        (row+nr, col+nc) not in visited and grid[row+nr][col+nc]!=0):
                        visited.add((row+nr, col+nc))
                        q.append((row+nr, col+nc))
            return area
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visited or grid[r][c]==0:
                    continue
                curr = bfs(r,c)
                ans = max(ans, curr)
        return ans