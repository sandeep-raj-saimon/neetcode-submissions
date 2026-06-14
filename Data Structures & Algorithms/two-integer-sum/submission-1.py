class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            num = nums[i]
            m[num] = i
        
        for i in range(len(nums)):
            num = nums[i]
            if m.get(target - num) is not None and m[target-num] != i:
                return [i, m.get(target-num)]