class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]

        product = 1
        for i in range(n):
            left[i] = nums[i]*product
            product = left[i]
        
        product = 1
        for i in range(n-1, -1, -1):
            right[i] = product * nums[i]
            product = right[i]
        print(left, right)
        ans = []
        for i in range(n):
            if i == 0:
                ans.append(right[i+1])
            elif i == n-1:
                ans.append(left[i-1])
            else:
                ans.append(right[i+1] * left[i-1])
        print(ans)
        return ans
            