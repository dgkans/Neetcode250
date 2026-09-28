from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each number appears
        counts = Counter(nums)

        # Frequency can range from 0 to n
        n = len(nums)
        buckets = []

        # Create a separate list for each frequency
        for i in range(n + 1):
            buckets.append([])

        # Put each number into its frequency bucket
        for number, frequency in counts.items():
            buckets[frequency].append(number)

        result = []

        # Check highest frequencies first
        for frequency in range(n, 0, -1):
            # Several numbers can have the same frequency
            for number in buckets[frequency]:
                result.append(number)

                # Stop once we have k numbers
                if len(result) == k:
                    return result