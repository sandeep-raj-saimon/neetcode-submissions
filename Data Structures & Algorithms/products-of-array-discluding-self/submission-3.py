class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [nums[-1]] * n
        right = [nums[0]] * n
        ans = [0] * n
        
        for i in range(1, n):
            right[i] = right[i-1] * nums[i]

        for i in range(n-2,-1,-1):
            left[i] = left[i+1] * nums[i]

        for i in range(n):
            if i > 0 and i < n-1:
                ans[i] = (right[i-1] * left[i+1])
            elif i > 0 and i == n-1:
                ans[i] = right[i-1]
            else:
                ans[i] = left[i+1]
        # ans[0] = int(left[0]/nums[0])
        # ans[-1] = int(right[-1]/nums[-1])
        return ans
        