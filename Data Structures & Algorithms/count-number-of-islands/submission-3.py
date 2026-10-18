class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        directions = [(1, 0),   # down
                      (-1, 0),  # up
                      (0, 1),   # right
                      (0, -1)   # left
                     ]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1" or (r,c) in visited:
                    continue

                count += 1

                stack = [(r, c)]
                visited.add((r, c))

                while stack:
                    x, y = stack.pop()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if (0<=nx<rows and
                            0<=ny<cols and
                            grid[nx][ny] == "1" and
                            (nx, ny) not in visited):

                            visited.add((nx, ny))
                            stack.append((nx, ny))

        return count
