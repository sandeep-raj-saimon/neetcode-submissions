from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = defaultdict(int)
        print(m)
        for i,num in enumerate(nums):
            print(num, m.get(num), i)
            if m.get(num) is not None and i - m.get(num) <=k:
                return True
            m[num] = i
        print(m)
        return False