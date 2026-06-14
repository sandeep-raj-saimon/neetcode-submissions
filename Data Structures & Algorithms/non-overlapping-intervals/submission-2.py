class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (-x[0], x[1]))
        print(intervals)
        prev = intervals[0]
        count = 0
        for interval in intervals[1:]:
            if interval[1] > prev[0]:
                count+=1
            else:
                prev = interval
        return count