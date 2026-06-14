class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in range(len(nums)):
            if m.get(nums[i]) is None:
                m[nums[i]] = 1
            else:
                return True
  
        return False