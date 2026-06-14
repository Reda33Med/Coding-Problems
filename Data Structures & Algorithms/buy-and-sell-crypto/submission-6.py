class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        max_left = [0] * len(prices)
        max_left[-1] = prices[-1]

        for i in range(len(prices) - 2 , -1 , -1):
            max_left[i] = max( max_left[i+1] , prices[i])

        for i in range(len(prices)):
            profit = max(profit , max_left[i] - prices[i])

            
        return profit