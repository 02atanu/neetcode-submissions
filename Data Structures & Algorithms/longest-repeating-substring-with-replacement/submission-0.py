class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counts = {} # Stores frequencies of the characters
        l = 0 # Left pointer
        result = 0

        max_freq = 0 # Frequency of highest repeating charcter (Optimization)
        for r in range(n):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            max_freq = max(max_freq, counts[s[r]])

            while (r - l + 1) - max_freq > k:
                counts[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        return result