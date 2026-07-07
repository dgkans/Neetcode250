class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            dist_sq = x*x + y*y
            heapq.heappush(heap,(dist_sq,point))
        res = []
        while k > 0:
            a, b = heapq.heappop(heap)
            res.append(b)
            k-=1
        return res

