#!/bin/python3

'''
Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window_start = 0
        window_end = 0
        char_frequency = {}
        max_length = 0
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            #then check the character is in the hashmap
            if right_char not in char_frequency:
                char_frequency[right_char] = 0  #store the character in the hashmap
            char_frequency[right_char] += 1     #increment the hashmap containing the character.
            
            #check if the len hashmap is greater than k. if yes we keep removing elements until we get the max length.
            while(len(char_frequency) > k):
                # we remove the element as we're trying to get the max length.
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1
            max_length = max(max_length, window_end-window_start + 1)
            
        return max_length
        
