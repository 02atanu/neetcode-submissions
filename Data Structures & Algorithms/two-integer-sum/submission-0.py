class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        # Store visited in the seen dict
        seen = {}

        for i, num in enumerate(nums):
            r = target - num
            if r in seen:
                return [seen[r], i]
            seen[num] = i