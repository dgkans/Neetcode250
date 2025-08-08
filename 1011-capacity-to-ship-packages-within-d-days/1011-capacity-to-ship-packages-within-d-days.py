class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            capacity,days_needed = 0,1
            for w in weights:
                capacity+=w
                if capacity > mid:
                    days_needed += 1
                    capacity = w
            if days_needed <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
