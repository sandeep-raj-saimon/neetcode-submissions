class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for num in nums:
            if m.get(num) is not None:
                return True
            else:
                m[num] = 1
        return False