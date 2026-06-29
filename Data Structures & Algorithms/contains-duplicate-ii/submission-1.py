from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(int)
        for i,num in enumerate(nums):
            if m.get(num) is not None and i - m.get(num) <=k:
                return True
            m[num] = i
        return False