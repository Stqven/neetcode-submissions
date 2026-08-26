class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if(len(s2) < len(s1)):
            return False

        s1_hash = defaultdict(int)

        for i in s1:
            s1_hash[i] += 1
        cur_letter = 0
        while(cur_letter + n <= len(s2)):
            s2_hash = defaultdict(int)
            l, r = cur_letter, cur_letter+n
            temp_sub = s2[l:r]
            for i in temp_sub:
                s2_hash[i] += 1
            if(s2_hash == s1_hash):
                return True
            cur_letter += 1
        return False

        