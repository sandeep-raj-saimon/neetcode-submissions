class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = float('-inf')
        left = 0
        right = len(height)-1

        while(left < right):
            min_height = min(height[left], height[right])
            curr_capacity = min_height * (right - left)
            max_capacity = max(curr_capacity, max_capacity)

            if height[left] <= height[right]:
                left +=1
            else:
                right -=1
        return max_capacity