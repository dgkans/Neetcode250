from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Best sum of a subarray ending at the current position
        current_sum = nums[0]

        # Largest sum found anywhere so far
        best_sum = nums[0]

        # The first element is already included
        for i in range(1, len(nums)):

            # A negative previous sum would make this number worse
            if current_sum < 0:
                current_sum = nums[i]

            else:
                # Extend the previous subarray through this position
                current_sum += nums[i]

            # Save the best result, even if later sums decrease
            best_sum = max(best_sum, current_sum)

        return best_sum