class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = []
        for i in range(1, len(prices)):
            diff.append(prices[i] - prices[i-1])
        print(diff)
        ans = 0
        max_ans = 0
        for d in diff:
            ans += d

            if ans < 0:
                ans = 0
            max_ans = max(ans, max_ans)
        return max_ans