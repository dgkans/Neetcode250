class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #brute force
        """ for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False """
        window = set()
        for i in range(len(nums)):
            if i > k:
                window.discard(nums[i - k - 1]) 
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False