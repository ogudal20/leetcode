class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window_start = 0
        window_end = 0
        max_length = 0
        distinct_chars = {}
        
        for window_end in range(len(s)):
            right = s[window_end]
            if right not in distinct_chars:
                distinct_chars[right] = 0
            distinct_chars[right] += 1
            
            while(len(distinct_chars) > k):
                left = s[window_start]
                distinct_chars[left] -= 1
                if distinct_chars[left] == 0:
                    del distinct_chars[left]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length 