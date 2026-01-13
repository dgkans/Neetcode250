class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outer = [[]]
        for i in nums:
            inner = []
            for j in outer:
                inner_ele = [i] + j
                inner.append(inner_ele)
            outer += inner
        return outer