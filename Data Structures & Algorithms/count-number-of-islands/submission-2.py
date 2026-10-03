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

        def dfs(r, c) -> None:
            # Casos donde no debo consultar
            if (
                r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or grid[r][c] == "0"
                or (r,c) in visited
            ):
                return
             # Si llegué aquí, la celda es válida (1)
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def dfs(r, c) -> None:

            stack = [(r,c)]
            visited.add((r,c))

            while stack:
                row, col = stack.pop() # LIFO

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        stack.append((nr, nc))
        
        
        def bfs(r, c) -> None:
            queue = [(r, c)]
            visited.add((r,c))

            while queue:
                row, col = queue.pop(0) # FIFO
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

