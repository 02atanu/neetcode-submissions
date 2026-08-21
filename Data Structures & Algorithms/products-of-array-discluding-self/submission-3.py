class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        #For optimization
        zero_count = 0

        # Store prefix product and suffix product
        result = [1]*l
        prefix = 1
        suffix = 1
        for i in range(l):
            # Double 0 optimization
            if zero_count > 1:
                 return [0] * l
            
            # Update prefix
            result[i] *= prefix
            prefix = prefix * nums[i]

            # Update suffix
            result[-i-1] *= suffix
            suffix = suffix * nums[-i-1]

            # Double 0 optimization
            if nums[i] == 0:
                zero_count += 1

        # Return products
        return result