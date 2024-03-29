class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        for c, i in count.items():
            freq[i].append(c)
        
        result = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                result.append(j)
            if len(result) == k:
                return result