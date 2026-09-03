class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Start with first and last item
        i = 0
        j = n - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, min(heights[i], heights[j]) * (j - i))

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return max_area