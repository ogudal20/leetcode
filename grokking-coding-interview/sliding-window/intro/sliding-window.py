#!/usr/bin/python3

'''
 Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

 Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

 Output: [2.2, 2.8, 2.4, 3.6, 2.8]
 '''

def find_averages_of_subarrays(K, arr):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, we don't need to slide if we've not hit the required window size of 'k'
        if windowEnd >= K - 1:
            result.append(windowSum / K) # Calculate the average
            windowSum -= arr[windowStart] # Subtract the element going out.
            windowStart += 1 # slide the window ahead 
    return result

def main():
    import pdb
    pdb.set_trace()
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: ", str(result))

main()
