class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}
        for index, num in enumerate(nums):
            m[num] = index

        count = 0
        max_count = float('-inf')

        for index, num in enumerate(nums):
            while m.get(num) is not None:
                num -=1
                count+=1
                max_count = max(max_count, count)
            count=0
        return max_count if max_count != float('-inf') else 0