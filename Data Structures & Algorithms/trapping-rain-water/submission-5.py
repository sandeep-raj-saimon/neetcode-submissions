class Solution:
    def trap(self, height: List[int]) -> int:
        # for each element, we need to store max element to its left and right

        n = len(height)
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        stack = []
        stack.append(height[0])

        for i in range(1,n-1):
            h = height[i]

            if h < stack[-1]:
                max_left[i] = stack[-1]
            else:
                stack.append(h)

        stack = []
        stack.append(height[-1])

        for i in range(n-2, 0, -1):
            h = height[i]

            if h < stack[-1]:
                max_right[i] = stack[-1]
            else:
                stack.append(h)

        water = 0
        for i in range(1,n-1):
            water += max(0, min(max_left[i], max_right[i]) - height[i])
        return water