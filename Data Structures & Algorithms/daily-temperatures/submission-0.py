class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if len(stack) == 0:
                stack.append([temp, i])
            else:
                while len(stack) != 0 and stack[-1][0] < temp:
                    last_element = stack[-1][0]
                    last_element_index = stack[-1][1]
                    result[last_element_index] = abs(i-last_element_index)
                    stack.pop()
                stack.append([temp, i])
        print(result)
        return result