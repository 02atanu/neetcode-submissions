class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq_map = [0] * 26
        s2_freq_map = [0] * 26

        for i in range(len(s1)):
            s1_freq_map[ord(s1[i]) - ord('a')] += 1
            s2_freq_map[ord(s2[i]) - ord('a')] += 1

        if s1_freq_map == s2_freq_map: # Check if it's a match from the start
            return True

        # Sliding window starts after the length of s1
        l = 0 # Left pointer
        for r in range(len(s1), len(s2)):
            s2_freq_map[ord(s2[r]) - ord('a')] += 1
            s2_freq_map[ord(s2[l]) - ord('a')] -= 1
            l +=1

            if s1_freq_map == s2_freq_map:
                return True
        return False