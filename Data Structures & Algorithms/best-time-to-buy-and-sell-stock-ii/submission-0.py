class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            #compare with next day, if it's bigger incrase profit by diff

            if i != len(prices)-1 and prices[i+1]> prices[i]:
                profit+= prices[i+1]-prices[i]
        return profit
