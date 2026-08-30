from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #parse words, make list of 0 and 1s
        if len(s) != len(t):
            return False

        word1 = defaultdict(int)
        word2 = defaultdict(int)

        for i in range(len(s)):
            word1[s[i]] += 1
            word2[t[i]] += 1

        return word1 == word2
        
        

            
