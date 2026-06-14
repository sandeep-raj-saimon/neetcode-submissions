class Solution:
    """
    if sum is odd or len of arr is 1, then ans is False
    otherwise we need to compute
    we need to check whether there exists a subset whose sum is half of total sum of arr.
    if yes then True else False
    """
    def __init__(self):
        self.nums = None
        self.target = None
        self.dp = None

    def recurse(self, index = 0, curr_sum = 0):
        if curr_sum > self.target or index >= len(self.nums):
            return False
        
        if self.dp[index][curr_sum] is not None:
            return self.dp[index][curr_sum]

        if curr_sum == self.target:
            return True
        self.dp[index][curr_sum] = (self.recurse(index+1, curr_sum + self.nums[index]) or self.recurse(index+1, curr_sum))
        return self.dp[index][curr_sum]

    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        total_sum = sum(nums)
        
        if total_sum % 2 == 1:
            return False
        self.nums = nums
        self.target = int(total_sum/2)

        self.dp = [[None for _ in range(0, self.target+1)] for _ in range(len(nums))]
        return self.recurse()
        # return self.ans
        # print(self.dp)
        # return self.dp[-1][-1]
    

