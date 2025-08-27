class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        
        while low < high:
            mid = (low + high) // 2
            sumsofar = 0
            subarrays = 1
            for num in nums:
                if num + sumsofar <=mid:
                    sumsofar += num
                else:
                    subarrays+=1
                    sumsofar = num
            if subarrays <= k:
                high = mid
            else:
                low = mid + 1
        return high
