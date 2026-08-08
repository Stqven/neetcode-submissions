class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #parse the string
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for letter in i:
                #make some type of count list * 26 
                #that list is the key:[word, word]
                letter = ord(letter) - 97
                count[letter] += 1
            res[tuple(count)].append(i)
        
        return(list(res.values()))