class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        ans = None

        while left <= right:
            total_days = 0
            mid = (left+right)//2

            curr_weight = 0
            for weight in weights:
                if (curr_weight + weight) > mid:
                    total_days+=1
                    curr_weight = 0
                curr_weight += weight
            if curr_weight > 0:
                total_days+=1
            
            if total_days > days:
                left = mid+1
                ans = left
            else:
                right = mid-1
            
        return left
                

