class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre = []

        for i in range(1, len(prices)):
            pre.append(prices[i]-prices[i-1])
        
        curr = 0
        ans = 0

        for i in pre:
            curr += i
            if curr < 0:
                curr = 0
            ans = max(ans, curr)
        return ans