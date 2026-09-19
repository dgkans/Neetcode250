from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])

        # Stores rotten oranges waiting to spread rot
        queue = deque()

        # Track remaining fresh oranges and elapsed minutes
        fresh = 0
        minutes = 0

        # Find all starting rotten oranges and count fresh ones
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1

                # All starting rotten oranges spread together
                elif grid[row][col] == 2:
                    queue.append((row, col))

        # Row and column changes: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Keep spreading while rotten and fresh oranges remain
        while queue and fresh > 0:

            # Only process this many oranges during this minute
            level_size = len(queue)

            for _ in range(level_size):
                # Remove the oldest orange from the queue
                row, col = queue.popleft()

                # Check its four neighboring cells
                for row_change, col_change in directions:

                    # Calculate the neighbor's position
                    next_row = row + row_change
                    next_col = col + col_change

                    # Skip neighbors outside the grid
                    if (
                        next_row < 0
                        or next_col < 0
                        or next_row >= rows
                        or next_col >= cols
                    ):
                        continue

                    # Skip empty cells (0) and rotten oranges (2)
                    if grid[next_row][next_col] != 1:
                        continue

                    # Mark rotten now to prevent duplicate additions
                    grid[next_row][next_col] = 2

                    # One fewer fresh orange remains
                    fresh -= 1

                    # This orange spreads rot during the next minute
                    queue.append((next_row, next_col))

            # One full level of spreading takes one minute
            minutes += 1

        # All oranges are rotten, or none were fresh initially
        if fresh == 0:
            return minutes

        # Some fresh oranges could not be reached
        return -1