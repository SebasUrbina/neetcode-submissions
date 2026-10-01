class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        profit = prices[i+t] - prices[i]
        
        Find the window that maximizes our profit.

        find the minimum index before k and maximum 
        10, 1, 5, 6, 7, 1
        l               r
        """ 

        # Brute force
        # profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         currentProfit = prices[j] - prices[i]
        #         profit = max(profit, currentProfit)

        # return max_profit

        # Simple for loop
        min_price = 9999
        max_profit = 0

        for p in prices:
            min_price = min(p, min_price)

            max_profit = max(max_profit, (p-min_price))
        # return max_profit

        # using while
        maxP = 0
        l, r = 0, 1 # buy low, sell high

        while r < len(prices):

            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r +=1
        return maxP





        