class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for p in prices:
            if p > buy_price:
                diff = p - buy_price
                profit = max(diff,profit)
            else:
                buy_price = p
        if profit >= 0:
            return profit
        else:
            return 0
                
