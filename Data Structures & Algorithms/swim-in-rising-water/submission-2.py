class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        minheap = []
        maxheight = grid[0][0]
        heapq.heappush(minheap, (maxheight, (0,0)))

        while minheap:
            height, pos = heapq.heappop(minheap)
            if pos in visited:
                continue
            visited.add(pos)
            maxheight = height
            if pos == (ROWS-1,COLS-1):
                break
            neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
            for n in neighbors:
                cr = pos[0]+n[0]
                cc = pos[1]+n[1]
                if cr<0 or cc<0 or cr==ROWS or cc ==COLS or (cr,cc) in visited:
                    continue
                currmax = max(height, grid[cr][cc])
                heapq.heappush(minheap,(currmax,(cr,cc)))
        return maxheight