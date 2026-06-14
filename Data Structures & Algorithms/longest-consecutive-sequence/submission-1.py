class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        nums.sort()
        max_count = float('-inf')
        count = 1

        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                pass
            elif num == prev + 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
            prev = num
        return max(max_count, count)
