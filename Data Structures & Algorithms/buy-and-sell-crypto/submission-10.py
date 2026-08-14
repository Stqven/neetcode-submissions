class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while r != len(prices):
            if(l < r) and prices[r] - prices[l] > 0:
                diff = prices[r] - prices[l]
                profit = max(diff, profit)
            else:
                l = r
            r += 1
        return profit