class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hash_map = defaultdict(int)
        #sorting: 0(nlogn)
        #hashmap = O(n),O(n), 
        #for loop:
            #is there a prev ?? if not then we can continue if not go next
            #going consecutive and looking it up in the hash, accum for each
        
        for i in nums:
            hash_map[i] += 1
        for i in nums:
            if i-1 not in hash_map:
                length = 1
                #check how many more are in the hashmap in sequential order
                while(length + i in hash_map):
                    length += 1
                res = max(length, res)
        return res