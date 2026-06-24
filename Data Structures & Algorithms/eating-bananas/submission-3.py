import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed = 1
        max_speed = max(piles)
        ans = None
        while min_speed <= max_speed:
            mid = (min_speed + max_speed)//2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i]/mid)

            if time <= h:
                ans = mid
                max_speed = mid-1
            else:
                min_speed = mid+1
        return ans