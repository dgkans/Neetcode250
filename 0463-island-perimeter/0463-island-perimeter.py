from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = []

        for row in range(rows):
            visited.append([False] * cols)

        def dfs(row, col):
            # Crossing the grid boundary exposes one land side.
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 1

            # Reaching water exposes one land side.
            if grid[row][col] == 0:
                return 1

            # Visited land is an internal connection, not a boundary.
            if visited[row][col] == True:
                return 0

            visited[row][col] = True

            top = dfs(row - 1, col)
            bottom = dfs(row + 1, col)
            left = dfs(row, col - 1)
            right = dfs(row, col + 1)

            return top + bottom + left + right

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    # One DFS covers the only island.
                    return dfs(row, col)

        # No land would mean no perimeter.
        return 0