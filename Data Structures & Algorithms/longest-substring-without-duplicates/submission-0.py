class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find a way to know they are not the same
        l, r = 0,0
        top_len = 0
        hash_map = defaultdict(int)
        while r < len(s):
            if(s[r] not in hash_map):
                hash_map[s[r]] += 1
                top_len = max(top_len, len(hash_map))
                r += 1

            else:
                while s[r] in hash_map:
                    del hash_map[s[l]]
                    l += 1
        return top_len
                


