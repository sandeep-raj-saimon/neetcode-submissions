"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals = sorted(intervals, key = lambda x: x.start)
        ans = intervals[0]

        possible = True
        for interval in intervals[1:]:
            if interval.start < ans.end:
                return False
            ans = interval
        return True