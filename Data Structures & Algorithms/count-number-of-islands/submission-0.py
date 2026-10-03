class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS: Depth first search -> stack
        BFS: Breadth first seach -> queue
        [
            ["0","1","1","1","0"],
            ["0","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        """
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()
        islands = 0
        
        def bfs(r, c) -> None:
            queue = [(r, c)]
            visited.add((r,c))

            while queue:
                row, col = queue.pop(0) # choose a row, col from queue
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands

