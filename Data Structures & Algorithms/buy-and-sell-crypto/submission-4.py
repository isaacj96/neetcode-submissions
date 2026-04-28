class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0

        for r, rval in enumerate(prices):
            if rval - prices[l] > res:
                res = max(rval - prices[l], res)
            if prices[l] > rval:
                l = r

        return res