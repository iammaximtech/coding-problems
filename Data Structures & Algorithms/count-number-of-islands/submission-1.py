class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0
        rows =len(grid)
        cols =len(grid[0])
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            length = 0
            while q:
                length = len(q)
                for i in range(length):
                    row, col = q.popleft()
                    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
                    for nr, nc in neighbors:
                        if (row+nr>=0 and row+nr<rows and col+nc>=0 and col+nc<cols and
                        (row+nr, col+nc) not in visited and grid[row+nr][col+nc]!="0"):
                            visited.add((row+nr, col+nc))
                            q.append((row+nr, col+nc))
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visited or grid[r][c]=="0":
                    continue
                bfs(r,c)
                ans+=1
        return ans
            
            
        