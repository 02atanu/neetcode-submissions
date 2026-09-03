class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  
        nums.sort()
        target = 0
        result = []

        i = 0
        while i < n -2:
            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                elif s < target:
                    j += 1
                else:
                    k -= 1
            while i < n-2 and nums[i] == nums[i+1]:
                i += 1
            i += 1

        return result