class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window, replace if we find another letter
        #replace wwith most seen letter
        #if we find another letter that does not fit with our current we move
        #the left pointer + 1
        #add r, check if it is the most frequent,
        # move r, if new letter we can replace -1 from k
        #if not jist keep going
        #always move r 
        # valid if the difference of most char - other char
        hash_map = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            hash_map[s[r]] += 1
            while(r - l + 1) - max(hash_map.values()) > k:
                hash_map[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res




