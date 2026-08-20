from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_counts = defaultdict(list)
        
        for word in strs:
            counts = [0] * 26
            for char in word:
                counts[ord(char) - ord('a')] += 1

            word_counts[tuple(counts)].append(word)
        return list(word_counts.values())