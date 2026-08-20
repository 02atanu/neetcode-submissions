class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return False
            
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
