from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        m = defaultdict(int)
        count = 1
        for i in range(len(nums)):
            m[nums[i]] = 1

        for i in range(len(nums)):
            if m.get(nums[i]-1) is None:
                pass
            else:
                curr_num = nums[i] - 1
                curr_count = 0
                while m.get(curr_num) is not None:
                    curr_num+=1
                    curr_count+=1
                count = max(curr_count, count)
        return count