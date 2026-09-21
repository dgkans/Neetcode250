from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Start with the widest possible container
        left = 0
        right = len(height) - 1

        # Largest area found so far
        best_area = 0

        # A container needs two different boundaries
        while left < right:
            width = right - left

            # The shorter line limits the water level
            water_height = min(height[left], height[right])
            area = width * water_height

            # Save the area before changing either boundary
            best_area = max(best_area, area)

            # Discard the shorter boundary; either can move on a tie
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return best_area