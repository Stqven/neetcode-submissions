class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hash_map = defaultdict(int)
        for i in nums: 
            hash_map[i] += 1
        
        #parse and find the largest val x amount of times
        #Sort it and return it going down
        #(o(n) + nlogn)

        my_dict = list(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        
        for s in range(k):
            res.append(my_dict[s][0])
        return res
