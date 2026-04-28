class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r, rval in enumerate(prices):
            if prices[l] > rval:
                l = r
            else:
                res = max(rval - prices[l], res)

        return res