class Solution:
    def __init__(self):
        self.ans = 0
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return nums[0]

        if n == 2:
            return max(nums[:2])
        # for every index, we can choose it or not
        # def recurse(idx, curr_sum=0):
        #     if idx == 0:
        #         return nums[0]
        #     if idx == 1:
        #         return max(nums[:2])

        #     current = nums[idx] + curr_sum + recurse(idx-2)
        #     skip = curr_sum + recurse(idx-1)
        #     return max(current, skip)
        # return recurse(n-1)

        dp = [-1 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        def recurse(idx, curr_sum=0):
            # if idx == 0:
            #     return nums[0]
            # if idx == 1:
            #     return max(nums[:2])
            if dp[idx] != -1:
                return dp[idx]

            current = nums[idx] + curr_sum + recurse(idx-2)
            skip = curr_sum + recurse(idx-1)
            dp[idx] = max(current, skip)
            return dp[idx]
        recurse(n-1)
        return dp[-1]