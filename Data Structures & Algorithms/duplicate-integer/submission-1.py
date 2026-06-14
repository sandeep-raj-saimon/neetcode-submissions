class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for num in nums:
            if m.get(num) is None:
                m[num] =1 
            else:
                m[num] +=1

        for value in m.values():
            if value > 1:
                return True
        return False