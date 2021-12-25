class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least_cost = 10 ** 4
        max_profit = 0
        
        for price in prices:
            least_cost = min(price, least_cost)
            max_profit = max(max_profit, price-least_cost)
            
        return max_profit
        