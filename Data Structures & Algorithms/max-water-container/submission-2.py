class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        curr = 0
        max_water = 0


        while (left < right):
            curr = min(heights[left], heights[right]) * (right - left)
            print(curr)
            max_water = max(curr, max_water)

            if heights[left] < heights[right]:
                left+=1
            else:
                right -=1
        return max_water