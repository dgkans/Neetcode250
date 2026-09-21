from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Lists sort by start first, then by end when starts are equal
        intervals.sort()

        # Begin with a copy of the first interval
        merged = [[intervals[0][0], intervals[0][1]]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            # The final interval already stored in the result
            last_interval = merged[-1]

            # Touching endpoints also count as overlapping
            if start <= last_interval[1]:

                # Keep the farther end; the current interval may be nested
                last_interval[1] = max(last_interval[1], end)

            else:
                # No overlap, so begin a separate interval
                merged.append([start, end])

        return merged