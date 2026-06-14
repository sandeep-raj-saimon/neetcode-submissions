class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr = [0] * len(prices)

        for i in range(len(prices)-1):
            arr[i] = prices[i+1] - prices[i]

        max_sum = float('-inf')
        curr_sum = 0

        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum < 0:
                curr_sum = 0
            max_sum = max(max_sum, curr_sum)
        return max_sum


