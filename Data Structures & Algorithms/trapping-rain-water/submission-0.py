class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i = 0 # Left pointer
        j = n-1 # Right Pointer

        left_max = height[i] # Left wall
        right_max =  height[j] # Right wall

        total = 0

        while i < j:
            if left_max < right_max:
                i += 1
                left_max = max(left_max, height[i])
                total += left_max - height[i]
            else:
                j -= 1
                right_max = max(right_max, height[j])
                total += right_max - height[j]

        return total