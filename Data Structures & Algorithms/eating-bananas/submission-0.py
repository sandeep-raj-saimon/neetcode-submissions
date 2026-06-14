from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)

        min_speed = 0

        while(left <= right):
            speed = (left+right)//2

            time = 0
            for pile in piles:
                time += ceil(pile/speed)
            
            if time > h:
                left = speed+1
            else:
                right = speed -1
                min_speed = speed
        return min_speed