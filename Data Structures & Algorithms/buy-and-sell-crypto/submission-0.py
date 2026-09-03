class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) in {0, 1}:
            return 0
        
        buy, sell, max_profit = prices[0], prices[0], 0

        for p in prices:
            if p < buy:
                buy = sell = p
            elif p > sell:
                sell = p
            
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit
                
        return max_profit