class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # we need to store how many elements are consecutively bigger
        # on left and right of the current element
        n = len(heights)
        left = [0]*n
        right = [0]*n

        stack = []
        for i, height in enumerate(heights):
            while stack and height <= stack[-1][0]:
                e = stack.pop()
                left[i] += left[e[1]] + 1
            stack.append([height,i])
        
        stack = []
        for i, height in reversed(list(enumerate(heights))):
            while stack and height <= stack[-1][0]:
                e = stack.pop()
                right[i] += right[e[1]] + 1
            stack.append([height,i])

        ans = float('-inf')
        for i in range(n):
            ans = max(ans, (heights[i] * (left[i] + right[i] +1)))
        return ans