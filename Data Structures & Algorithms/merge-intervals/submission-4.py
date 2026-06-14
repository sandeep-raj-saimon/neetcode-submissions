class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort intervals based on the second element
        intervals = sorted(intervals, key=lambda x: x[0])
        
        ans = [intervals[0]]  # Start with the first interval

        for interval in intervals[1:]:
            last = ans[-1]  # Get the last interval in the result

            # If the current interval overlaps with the last one, merge them
            if last[1] >= interval[0]:
                ans[-1] = [last[0], max(last[1], interval[1])]  # Merge intervals
            else:
                ans.append(interval)  # No overlap, so just append the current interval
                
        return ans