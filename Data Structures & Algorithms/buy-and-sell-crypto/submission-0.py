class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # current_profit = 0
        # for buy in range(len(prices)):
        #     for sell in range(buy+1, len(prices)):
        #         if prices[buy] > prices[sell]:
        #             sell += 1

        #         else:
        #             prices[buy] < prices[sell]
        #             profit = prices[sell] - prices[buy]
        #             current_profit= max(current_profit, profit)

        # return current_profit
        left , right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right]- prices[left]
                max_profit = max(max_profit, profit)

            else:
                left = right
            right += 1

        return max_profit

        


        