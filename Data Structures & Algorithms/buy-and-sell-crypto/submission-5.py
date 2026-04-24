class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        purchase_price = prices[0]

        for today_price in prices:
            max_profit = max(max_profit, today_price - purchase_price)
            purchase_price = min(purchase_price, today_price)
        return max_profit