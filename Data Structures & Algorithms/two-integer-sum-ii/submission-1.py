class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) -1

        while (first < last):
            current_sum = numbers[first] + numbers[last]
            if current_sum == target:
                return [first+1, last+1]
            elif current_sum < target:
                first += 1
            else:
                last -= 1
        