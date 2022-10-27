class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # get count of each number
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # add the count of each number in the list.
        for i, c in count.items():
            freq[c].append(i)
            
        # Check if top k results.
        result = []
        for i in range(len(nums), 0, -1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
            