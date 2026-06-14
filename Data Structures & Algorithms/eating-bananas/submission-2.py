from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)
        ans = float('inf')
        while(left < right):
            speed = (left + right)//2
            print('speed is ', speed)
            time = 0
            for pile in piles:
                time += ceil(pile/speed)
            
            if time > h:
                left = speed+1
            else:
                right = speed
                ans = min(ans, speed)
        return ans