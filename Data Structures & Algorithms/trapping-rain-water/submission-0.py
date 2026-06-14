class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]*len(height)
        max_right = [0]*len(height)

        stack = []
        for i in range(len(height)-1):
            h = height[i]
            if len(stack) == 0:
                stack.append(h)
            else:
                if (stack[-1] >= h):
                    max_left[i] = stack[-1]
                else:
                    stack.append(h)
        
        stack = []
        for i in range(len(height)-1, 0, -1):
            h = height[i]
            if len(stack) == 0:
                stack.append(h)
            else:
                if (stack[-1] >= h):
                    max_right[i] = stack[-1]
                else:
                    stack.append(h)
        
        water = 0
        for i in range(len(height)):
            curr_water = min(max_left[i], max_right[i])  - height[i]
            if curr_water > 0:
                water += curr_water
        return water