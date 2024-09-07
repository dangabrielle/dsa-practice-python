# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.# 

# This solution uses the sliding window technique.
class Solution:
    def maxProfit(self, prices):
        max_prof = 0
        i = 1
        j = 0

        while i < len(prices):
            # continue to calc profit and update max_prof each iteration
            profit = prices[i] - prices[j]
            if profit > max_prof:
                max_prof = profit
          
            # change j position to be the lowest value in the array before prices[i]
            if prices[i] < prices[j]:
                j = i
            i += 1
        
        return max_prof