class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        pre = [nums[0]]
        for i in range(1, len(nums)):
            pre.append(nums[i] * pre[i-1])
         
        post = [0]*len(nums)
        post[-1] = nums[-1]

        for i in range(len(nums)-2, -1,-1):
            post[i] = (nums[i] * post[i+1])
        
        print(pre, post)
        ans = [0]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                ans[i] = post[i+1]
            elif i == len(nums)-1:
                ans[i] = pre[i-1]
            else:
                ans[i] = pre[i-1]*post[i+1]
        return ans
            