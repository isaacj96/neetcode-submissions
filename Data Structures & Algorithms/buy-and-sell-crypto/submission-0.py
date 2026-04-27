class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        window = set()
        buy = 0
        profit = 0

        for sell, _ in enumerate(prices):
            if prices[sell] < prices[buy]:
                prices[buy] = prices[sell]
            if prices[sell] - prices[buy] > profit:
                profit = prices[sell] - prices[buy]
        return profit