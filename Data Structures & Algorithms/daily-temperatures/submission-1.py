class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result =[0]*n
        print(result)
        stack = []

        
        for i,temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                e = stack.pop()
                result[e[1]] = i-e[1]
            stack.append([temperature, i])
        return result
