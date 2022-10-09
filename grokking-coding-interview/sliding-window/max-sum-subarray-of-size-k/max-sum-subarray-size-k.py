#!/usr/bin/python3

'''
Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

'''

def max_sum_of_subarray(K, arr):
    result = 0
    windowSum, windowStart = 0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= K - 1:
            if windowSum > result:
                result = windowSum
            windowSum -= arr[windowStart]
            windowStart += 1 
    return result

def main():
    result = max_sum_of_subarray(2, [2, 3, 4, 1, 5])
    print("Max sum of subarray of size K: ", result)

main()
    
