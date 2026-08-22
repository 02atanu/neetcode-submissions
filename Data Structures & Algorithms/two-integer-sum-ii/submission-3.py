class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1, 2]

        i = 0 # Intially points to the first element
        j = len(numbers) - 1 # Initially points to last element
        while i < j:
            x = numbers[i]
            y = numbers[j]
            if x + y == target:
                return [i+1, j+1]
            elif x + y < target:
                i += 1
            else:
                j -= 1



        