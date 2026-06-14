from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for index,num in enumerate(nums):
            m[num] = index

        for index, num in enumerate(nums):
            diff = target - num
            if m.get(diff) is not None and m.get(diff) != index:
                return [index, m.get(diff)]
        return False
            