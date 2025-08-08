class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            cap,dy = 0,1
            for w in weights:
                cap+=w
                if cap > mid:
                    dy += 1
                    cap = w
            if dy <= days:
                high = mid - 1
            else:
                low = mid+1
        return low
