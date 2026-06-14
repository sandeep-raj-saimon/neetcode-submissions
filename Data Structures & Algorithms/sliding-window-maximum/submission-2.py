class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [max(nums[:k])]
        print(len(nums)-k)
        for i in range(1, len(nums)-k+1):
            ans.append(max(nums[i:i+k]))
        return ans