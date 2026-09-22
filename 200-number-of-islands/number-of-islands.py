class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                directions = [
                    [1, 0],
                    [-1, 0],
                    [0, 1],
                    [0, -1]
                ]

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
        