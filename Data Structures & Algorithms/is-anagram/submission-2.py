class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return false if the lengths are different
        if len(s) != len(t):
            return False
        
        counts = {}

        # Create a Hashmap for storing counts of s
        for i in s:
            counts[i] = counts.get(i, 0) + 1

        # Check the hashmap for counts of t
        for j in t:
            if j not in counts:
                return False
            counts[j] -= 1
            if counts[j] < 0:
                return False
        return True
