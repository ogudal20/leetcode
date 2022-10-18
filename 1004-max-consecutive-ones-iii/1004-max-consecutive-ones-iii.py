class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ans = 0
        curr = 0
        right = 0
        left = 0
        
        for right in range(len(nums)):
            # check if there is a 0
            if nums[right]  == 0:
                curr += 1
            
            while(curr > k):
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        