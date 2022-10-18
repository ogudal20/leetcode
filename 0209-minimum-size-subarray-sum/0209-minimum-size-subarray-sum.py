class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_start = 0
        window_end = 0
        min_length = float("inf")
        curr_sum = 0
        
        for window_end in range(len(nums)):
            right = nums[window_end]
            curr_sum += right
            
            while(curr_sum >= target):
                min_length = min(min_length, window_end - window_start + 1)
                curr_sum -= nums[window_start]
                window_start += 1
        if min_length == float("inf"):
            return 0
        return min_length