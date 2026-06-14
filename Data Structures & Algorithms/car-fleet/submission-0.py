class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remaining = []
        i = 0
        for pos in position:
            remaining.append([target - pos, speed[i]])
            i+=1
        remaining = sorted(remaining, key=lambda x:x[0])

        stack = []
        for ele in remaining:
            distance = ele[0]
            speed = ele[1]
            if distance == 0:
                stack.append(-1)
            else:
                time = distance/speed
                if len(stack) == 0:
                    stack.append(time)
                else:
                    if time <= stack[-1]:
                        stack.append(stack[-1])
                    else:
                        stack.append(time)

        return len(set(stack))

