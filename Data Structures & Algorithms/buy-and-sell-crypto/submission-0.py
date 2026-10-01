class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        profit = prices[i+t] - prices[i]
        
        Find the window that maximizes our profit.

        find the minimum index before k and maximum 
        10, 1, 5, 6, 7, 1
        l               r
        """

        min_price = 9999
        max_profit = 0

        for p in prices:
            min_price = min(p, min_price)

            max_profit = max(max_profit, (p-min_price))


        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         currentProfit = prices[j] - prices[i]
        #         profit = max(profit, currentProfit)

        return max_profit





        