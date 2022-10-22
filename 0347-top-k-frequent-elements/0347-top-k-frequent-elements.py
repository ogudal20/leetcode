class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. define a hashmap 
        #2. loop through nums array
            #a. in each iteration add the num in hashmap if the don't exist with value 0
            #b. increment the value of key in the hashmap
        
        #3. sort the hashmap by the values from highest to lowest.
        #4. loop through the 0 to k elements
            # append the values in the hashmap to new list
        #5. return the list
        index = 0
        most_freq = {}
        result = []
        for i in nums:
            if i not in most_freq:
                most_freq[i] = 0
            most_freq[i] += 1
            
        most_freq = list(sorted(most_freq.items(), key=lambda item: item[1], reverse=True))
        
        for j in range((k)):
            result.append(most_freq[j][index])
        return result