class TimeMap:

    def __init__(self):
        self.time_series = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.time_series.get(key) is None:
            self.time_series[key] = []
    
        self.time_series[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if self.time_series.get(key) is None:
            return ""
        values = self.time_series.get(key)
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l+r)//2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1
        return res
