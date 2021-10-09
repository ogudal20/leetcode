"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
  
        match = {}
   
        for i in range(len(nums)):
            potentialMatch = target - nums[i]
            if potentialMatch in match:
                return [i, nums.index(potentialMatch)]
            else:
                match[nums[i]] = True
        
        return []

