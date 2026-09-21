from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = []
        ends = []

        # Collect all meeting start and end times
        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        # Process each kind of event in chronological order
        starts.sort()
        ends.sort()

        # Indices of the next start and end events
        start_index = 0
        end_index = 0

        # Current occupied rooms and highest demand seen
        active = 0
        rooms = 0

        # After all starts, room demand can only decrease
        while start_index < len(intervals):

            # A meeting starts before the next meeting ends
            if starts[start_index] < ends[end_index]:
                active += 1
                rooms = max(rooms, active)
                start_index += 1

            else:
                # Free a room first, including when times are equal
                active -= 1
                end_index += 1

        return rooms