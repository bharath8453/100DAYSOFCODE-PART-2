class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        # Loop through the price list
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))  
print(obj.maxProfit([1,2,3,4,5]))  
print(obj.maxProfit([7,6,4,3,1])) 