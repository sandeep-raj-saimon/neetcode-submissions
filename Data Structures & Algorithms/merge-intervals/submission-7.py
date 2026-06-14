class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        ans = [intervals[0]]
        for interval in intervals:
            last = ans[-1]

            if last[1] >= interval[0]:
                ans.pop()
                ans.append([last[0], max(interval[1], last[1])])
            else:
                ans.append(interval)
        return ans