class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        #For optimization
        zero_count = 0

        # Store prefix product and suffix product
        pp_and_sp = [[0,0] for _ in range(l)]
        prefix = 1
        suffix = 1
        for i in range(l):
            # Double 0 optimization
            if zero_count > 1:
                 return [0] * l
            
            # Update prefix
            pp_and_sp[i][0] = prefix
            prefix = prefix * nums[i]

            # Update suffix
            pp_and_sp[-i-1][1] = suffix
            suffix = suffix * nums[-i-1]

            # Double 0 optimization
            if nums[i] == 0:
                zero_count += 1

        # Return products
        return [ l[0]*l[1] for l in pp_and_sp]