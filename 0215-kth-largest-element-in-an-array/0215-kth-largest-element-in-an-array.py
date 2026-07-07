class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        val = 0
        while k > 0:
            val = heapq.heappop_max(nums)
            k-=1
        return val
            