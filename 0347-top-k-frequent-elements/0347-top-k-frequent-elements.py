class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the number of occurences for each num
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            
        # Going through each number that we counted.
        for n, c in count.items():
            freq[c].append(n)
            
        # get top k elements.
        # start in descending order to get top k elements.
        # start from the end of array to the start and decrement loop by 1
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        