class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        stack = []

        # for calculating max_left, we will start from left
        stack.append(heights[0])
        for i in range(1,n-1):
            height = heights[i]
            if height < stack[-1]:
                max_left[i] = stack[-1]
            else:
                stack.append(height)

        # for calculating max_right, we will start from right
        stack = [heights[-1]]
        for i in range(n-2, 0, -1):
            height = heights[i]
            if height < stack[-1]:
                max_right[i] = stack[-1]
            else:
                stack.append(height)
        
        # now we have max_left and max_right, we can now
        # calculate water container over each block
        curr_water = 0
        for i in range(1,n-1):
            curr_water += max(0, min(max_left[i], max_right[i]) - heights[i])
        return curr_water