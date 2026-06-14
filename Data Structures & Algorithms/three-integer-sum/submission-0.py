class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        after sorting we can use 2 pointer approach
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = n-1

            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                print('curr_sum', curr_sum)
                if curr_sum > 0:
                    r-=1
                elif curr_sum < 0:
                    l+=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while nums[l] == nums[l-1] and l < r:
                        print("ere")
                        l+=1
        return ans
            

