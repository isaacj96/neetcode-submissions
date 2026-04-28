class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        window = {}
        l = 0
        profittmp = 0
        res = 0

        for r, rval in enumerate(prices):
            if rval - prices[l] > profittmp:
                profittmp = rval - prices[l]
            if prices[l] > rval:
                l = r
            
            res = max(profittmp, res)

        return res