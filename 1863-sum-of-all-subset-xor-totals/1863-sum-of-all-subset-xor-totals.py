class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        allsum = 0
        for n in nums:
            allsum = allsum | n
        return allsum * (pow(2,len(nums)-1))
