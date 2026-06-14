class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remaining = []
        i = 0
        for pos in position:
            remaining.append([target - pos, speed[i]])
            i+=1
        remaining = sorted(remaining, key=lambda x:x[0])

        stack = []
        is_distance = False
        for ele in remaining:
            distance = ele[0]
            speed = ele[1]
            if distance == 0:
                is_distance = True
            else:
                time = distance/speed
                if len(stack) == 0:
                    stack.append(time)
                else:
                    if time > stack[-1]:
                        stack.append(time)

        return len(stack) + 1 if is_distance else len(stack)

