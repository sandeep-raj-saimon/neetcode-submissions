class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        res = float('-inf')
        for num in nums:
            curr = curr_max * num
            curr_max = max(
                curr_max * num,
                curr_min * num,
                num
                )
            curr_min = min(curr, curr_min * num, num)
            res = max(res, curr_max)
        return res
            