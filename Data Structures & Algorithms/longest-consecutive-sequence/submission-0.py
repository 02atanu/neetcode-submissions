class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            # Pick up the starts of the seq
            if num - 1 not in nums_set:
                current = num
                seq_len = 1
                while current + 1 in nums_set:
                    current += 1
                    seq_len += 1

                longest = max(longest, seq_len)
                
        return longest
        