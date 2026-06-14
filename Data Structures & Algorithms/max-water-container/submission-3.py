class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        curr_water = 0
        n = len(heights)
        i = 0
        j = n-1

        while i < j:
            curr_water = min(heights[i], heights[j]) * (j-i)
            max_water = max(curr_water, max_water)
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        return max_water
        
