class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        num_set = set(nums)
        max_count = 1

        for num in nums:
            if (num-1) not in num_set:
                length = 0
                while (num+length) in num_set:
                    length +=1
                max_count = max(max_count, length)
        return max_count