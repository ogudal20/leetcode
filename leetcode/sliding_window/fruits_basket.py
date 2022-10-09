#!/usr/bin/python3

'''
Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].

'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start = 0
        window_end = 0
        fruits_frequency = {}
        sum_fruits = 0
        
        for window_end in range(len(fruits)):
            right_char = fruits[window_end]
            if right_char not in fruits_frequency:
                fruits_frequency[right_char] = 0
            fruits_frequency[right_char] += 1
            
            while(len(fruits_frequency) > 2):
                left_char = fruits[window_start]
                fruits_frequency[left_char] -= 1
                if fruits_frequency[left_char] == 0:
                    del fruits_frequency[left_char]
                window_start += 1
            sum_fruits = max(sum_fruits, window_end-window_start +1)
            
        return sum_fruits
