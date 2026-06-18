class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        n = len(prices)
        for i in range(1,n):
            diff.append(prices[i] - prices[i-1])

        max_profit = float('-inf')
        curr_profit = 0

        for d in diff:
            curr_profit += d
            if curr_profit <= 0:
                curr_profit = 0

            max_profit = max(max_profit, curr_profit)
        
        return max_profit if max_profit != float('-inf') else 0