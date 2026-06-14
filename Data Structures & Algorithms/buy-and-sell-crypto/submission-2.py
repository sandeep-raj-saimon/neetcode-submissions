class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        preprocess = [prices[0]]
        for i in range(1, len(prices)):
            preprocess.append(prices[i] - prices[i-1])
        

        max_sum = float('-inf')
        curr_sum = 0

        for i in range(1,len(preprocess)):
            curr_sum += preprocess[i]

            if curr_sum < 0 :
                curr_sum = 0
            max_sum = max(max_sum, curr_sum)
        return max_sum if max_sum != float('-inf') else 0