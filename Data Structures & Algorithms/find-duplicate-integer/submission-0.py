from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = Counter(nums)
        for key in c:
            if c[key] > 1:
                return key
        