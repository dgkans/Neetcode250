import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # Negative prices make this a max heap for buy prices
        buy = []

        # Positive prices keep the cheapest sell at the root
        sell = []

        # Process batches in their original arrival order
        for price, amount, order_type in orders:
            if order_type == 0:
                # Match while sells exist and their cheapest price is affordable
                while amount > 0 and sell and sell[0][0] <= price:
                    sell_price, sell_amount = heapq.heappop(sell)

                    # Execute the smaller available quantity
                    matched = min(amount, sell_amount)
                    amount -= matched
                    sell_amount -= matched

                    # Return the unfilled portion of this sell batch
                    if sell_amount > 0:
                        heapq.heappush(sell, (sell_price, sell_amount))

                # Save the unfilled portion of the incoming buy
                if amount > 0:
                    heapq.heappush(buy, (-price, amount))

            else:
                # Convert the negative root price back before comparing
                while amount > 0 and buy and -buy[0][0] >= price:
                    negative_price, buy_amount = heapq.heappop(buy)

                    # Execute the smaller available quantity
                    matched = min(amount, buy_amount)
                    amount -= matched
                    buy_amount -= matched

                    # Keep the stored buy price negative when reinserting
                    if buy_amount > 0:
                        heapq.heappush(buy, (negative_price, buy_amount))

                # Save the unfilled portion of the incoming sell
                if amount > 0:
                    heapq.heappush(sell, (price, amount))

        # Sum quantities, not prices or numbers of batches
        total = 0
        for negative_price, amount in buy:
            total += amount

        for price, amount in sell:
            total += amount

        return total % (10**9 + 7)