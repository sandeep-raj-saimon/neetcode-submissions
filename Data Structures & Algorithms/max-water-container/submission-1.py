class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        i = 0
        j = len(heights) - 1


        while(i<j):
            curr_water = min(heights[i], heights[j]) * (j-i)
            if heights[i] >= heights[j]:
                j-=1
            else:
                i+=1
            water = max(water, curr_water)
        return water