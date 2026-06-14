class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        we must be greedy about the steps that we take, we always
        """
        if len(nums) == 1:
            return 0

        n = len(nums)
        steps = [0 for _ in range(n)]
        min_step = float('inf')
        for i in range(n-2, -1, -1):
            index = nums[i]+i
            if index >= n-1:
                steps[i] = 1
                min_step = 1
            else:
                min_step = min(min_step+1, 1+steps[index])
                steps[i] = min_step

        return min_step