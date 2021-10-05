
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        new_array = []
        
        for i in range(len(nums)):
            new_array = nums
        
        new_array.extend(nums)
                
            
        return new_array
     
