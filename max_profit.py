# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_index = 0
        max_index = 0
        next_min_index = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[min_index] and prices[i] < prices[next_min_index]:
                next_min_index = i

            elif prices[i] >= prices[max_index] or prices[i]-prices[next_min_index] > prices[max_index]-prices[min_index]:
                max_index = i
                if prices[next_min_index] < prices[min_index]:
                    min_index = next_min_index

        return 0 if max_index <= min_index else prices[max_index]-prices[min_index]
