import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed))
        position, speed = map(list, zip(*combined))
        times = []

        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            times.append(time)
        
        stack = []
        print(times)
        for time in times:
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)
        