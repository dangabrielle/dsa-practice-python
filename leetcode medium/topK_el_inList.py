class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        return [x[0] for x in result[:k]]
