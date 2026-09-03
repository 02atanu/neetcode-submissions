class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Start with first and last item
        i = 0
        j = n - 1
        max_area = 0
        while i < j:
            curr_height = min(heights[i], heights[j])
            max_area = max(max_area, curr_height * (j - i))

            # Skip to potential max_area
            while i < j and heights[i] <= curr_height:
                i += 1
            while i < j and heights[j] <= curr_height:
                j -= 1
            
        return max_area