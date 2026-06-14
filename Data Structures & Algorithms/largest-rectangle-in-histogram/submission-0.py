class Solution:
    def getSequence(self, heights):
        n = len(heights)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]

        stack = []
    
        for i in reversed(range(n)):
            count = 0
            while stack and heights[i] <= heights[stack[-1]]:
                count += right[stack.pop()] + 1
            
            right[i] = count
            stack.append(i)
        
        stack = []
        for i in (range(n)):
            count = 0
            while stack and heights[i] <= heights[stack[-1]]:
                count += left[stack.pop()] + 1
            
            left[i] = count
            stack.append(i)
        
        return [left, right]
        
        
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        we need two arrays for storing the left and right 
        """
        left, right = self.getSequence(heights)
        max_area = 0
        n = len(heights)
        for i in range(n):
            curr_area = heights[i] * (1 + left[i] + right[i])
            max_area = max(max_area, curr_area)
        return max_area
        