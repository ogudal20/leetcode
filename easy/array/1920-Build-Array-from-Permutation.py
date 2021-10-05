
# [0,2,1,5,3,4]
# [0,1,2,4,5,3]

## create a variable tracker
## create new array variable
## loop through the len of array
    ## get index of array and store in tracker in variable.
    ## append the tracker to new array.
##return new array


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        
        nums_pointer = 0
        new_array = []
        
        for i in range(len(nums)):
            nums_pointer = nums[i]
            new_array.append(nums[nums_pointer])
            
        return new_array
