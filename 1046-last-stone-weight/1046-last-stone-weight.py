class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            heapq.heapify_max(stones)
            while len(stones) > 1:
                y = heapq.heappop_max(stones)
                x = heapq.heappop_max(stones)
                if y != x:
                    val = y - x
                    heapq.heappush_max(stones, val) 
            return stones[-1] if stones else 0