class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [] 
        post = []
        res = []
        post_num = 1
        pre_num = 1

        #pre:[1,1,8,8]
        #post:[48,24,6,1]
        for i in nums:
            pre.append(post_num)
            post_num *= i
        for s in reversed(nums):
            post.append(pre_num)
            pre_num *= s
        post.reverse()
        for j in range(len(pre)):
            res.append(pre[j] * post[j]) 
        return res     


