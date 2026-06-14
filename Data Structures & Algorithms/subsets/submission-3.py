class Solution:
    def __init__(self):
        self.ans = []

    def generateSubset(self, nums, start = 0, stack=[]):
        self.ans.append(stack[:])

        for i in range(start, len(nums)):
            stack.append(nums[i])
            self.generateSubset(nums, i+1, stack)
            stack.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.generateSubset(nums)
        print(self.ans)
        return self.ans