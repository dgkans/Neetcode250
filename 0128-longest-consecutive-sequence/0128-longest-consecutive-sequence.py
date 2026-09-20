from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Remove duplicates and allow fast membership checks
        numbers = set(nums)

        # Remains 0 if the input is empty
        longest = 0

        # Iterate over unique numbers to avoid duplicate work
        for number in numbers:

            # A predecessor means this is not a sequence start
            if number - 1 in numbers:
                continue

            # Start a new sequence at this number
            current = number
            length = 1

            # Extend while the next consecutive number exists
            while current + 1 in numbers:
                current += 1
                length += 1

            # Keep the longest sequence found so far
            longest = max(longest, length)

        return longest