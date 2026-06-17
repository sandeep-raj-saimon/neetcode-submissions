class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        max_water = float('-inf')
        curr =0
        while l < r:
            curr = min(heights[l], heights[r]) * (r-l)
            max_water = max(max_water, curr)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max(max_water, curr)