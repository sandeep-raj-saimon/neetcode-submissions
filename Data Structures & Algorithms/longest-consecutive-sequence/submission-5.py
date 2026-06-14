from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = defaultdict(int)

        for num in nums:
            m[num]=1

        count = 0
        max_count = 0
        for num in nums:
            while m.get(num) is not None:
                print(num)
                count += 1
                num = num-1
            print()
            max_count = max(max_count, count)
            count = 0
        return max_count