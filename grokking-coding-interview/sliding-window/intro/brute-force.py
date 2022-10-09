#!/usr/bin/python3

'''
 Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

 Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

 Output: [2.2, 2.8, 2.4, 3.6, 2.8]
 '''

def find_averages_of_subarrays(K, arr):
    result = []
    for i in range(len(arr)-K+1):
        # find sum of next K elements
        _sum = 0.0
        for j in range(i, i+K):
            _sum += arr[j]
        result.append(_sum/K)
    return result

def main():
    import pdb
    pdb.set_trace()
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: ", str(result))

main()
