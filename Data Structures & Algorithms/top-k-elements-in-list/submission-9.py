class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        mostcommon = []

        for i in nums:
            counts[i] += 1

        for i in range(k):
            max_key = max(counts, key=counts.get)
            mostcommon.append(max_key)
            del counts[max_key]
        
        return mostcommon
