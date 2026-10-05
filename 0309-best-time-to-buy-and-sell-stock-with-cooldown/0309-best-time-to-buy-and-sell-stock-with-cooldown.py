from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Day 0: buy the first share or do nothing
        hold = -prices[0]
        rest = 0

        # Selling on day 0 is impossible
        sold = float("-inf")

        # Update the best profit for each end-of-day state
        for day in range(1, len(prices)):
            price = prices[day]

            # Use only yesterday's states for today's decisions
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            # Keep holding, or buy after a resting day
            hold = max(prev_hold, prev_rest - price)

            # Sell a share held yesterday
            sold = prev_hold + price

            # Keep resting, or complete the cooldown after a sale
            rest = max(prev_rest, prev_sold)

        # Finish without an unsold share
        return max(sold, rest)