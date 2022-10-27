class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        
        # if not the same length then can't be anagram.
        if len(s) != len(t):
            return False
        
        # then we check the number of characters in both strings if the same then its as anagram
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT