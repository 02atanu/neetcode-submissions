class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        # Store prefix product and suffix product
        pp_and_sp = [[0,0] for _ in range(l)]
        prefix = 1
        suffix = 1
        for i in range(l):
            # Update prefix
            pp_and_sp[i][0] = prefix
            prefix = prefix * nums[i]

            # Update suffix
            pp_and_sp[-i-1][1] = suffix
            suffix = suffix * nums[-i-1]
            
        # Return products
        return [ l[0]*l[1] for l in pp_and_sp]

        