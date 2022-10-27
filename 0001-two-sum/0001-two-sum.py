class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMatch = {}
        
        for i,counts in enumerate(nums):
            diff = target - counts
            if diff in prevMatch:
                return [prevMatch[diff], i]
            prevMatch[counts] = i
        return