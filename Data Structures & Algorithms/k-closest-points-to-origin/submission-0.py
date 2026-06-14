import heapq
class Solution:
    def __init__(self):
        self.origin = [0, 0]
    
    def calculateDistance(self, point):
        distance = math.sqrt((point[0] - self.origin[0])**2 + (point[1] - self.origin[1])**2)
        return distance

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        heapq.heapify(ans)
        for point in points:
            distance = self.calculateDistance(point)
            heapq.heappush(ans, (-distance, point))
            if len(ans) > k:
                heapq.heappop(ans)
        print(ans)
        answer = [i[1] for i in ans]
        print(answer)
        return answer
        