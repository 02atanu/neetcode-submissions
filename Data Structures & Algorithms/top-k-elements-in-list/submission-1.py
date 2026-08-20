class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        l = len(nums)
        buckets = [[] for _ in range(l+1)]
        result = []

        for n, count in freq.items():
            buckets[count].append(n)
            
        for i in range(l, 0, -1):
            if not buckets[i]:
                continue

            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return(result)