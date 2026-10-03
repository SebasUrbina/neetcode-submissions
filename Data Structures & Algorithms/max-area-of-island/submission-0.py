class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        islands = 0

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # not to consider
            if (
                r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or grid[r][c] == 0
                or (r, c) in visited
            ): 
                return 0
            
            visited.add((r,c))
            return (
                1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    currentArea = dfs(r,c)
                    maxArea = max(maxArea, currentArea)

        return maxArea

        