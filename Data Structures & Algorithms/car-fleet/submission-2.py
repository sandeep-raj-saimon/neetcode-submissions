class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        remaining = []
        for i, pos in enumerate(position):
            remaining.append([target - pos, speed[i]])
        remaining = sorted(remaining, key=lambda x:x[0])

        stack =[]
        is_already_present = False

        for remain in remaining:
            dis, speed = remain
            if dis == 0:
                is_already_present = True
            else:
                time = dis/speed
                if len(stack) == 0:
                    stack.append(time)
                else:
                    if time > stack[-1]:
                        stack.append(time)
        return len(stack) + 1 if is_already_present else len(stack) 