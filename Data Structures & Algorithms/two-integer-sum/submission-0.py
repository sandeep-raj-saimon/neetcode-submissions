class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if m.get(diff) is not None:
                return [m.get(diff), i]
            else:
                m[num] = i
        return []
            