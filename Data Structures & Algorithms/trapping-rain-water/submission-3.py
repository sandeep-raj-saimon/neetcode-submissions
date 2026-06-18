class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        stack = []

        stack.append(heights[0])
        
        for i in range(1,n-1):
            h = heights[i]
            if h < stack[-1]:
                max_left[i]=stack[-1]
            else:
                stack.append(h)

        stack=[]
        stack.append(heights[-1])

        for i in range(n-2, 0, -1):
            h = heights[i]
            if h < stack[-1]:
                max_right[i]=stack[-1]
            else:
                stack.append(h)

        print(max_left)
        print(max_right)

        water = 0

        for i in range(n):
            water+= max(0, min(max_left[i], max_right[i]) - heights[i])

        return water