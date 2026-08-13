class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        mid = len(nums)//2
        if len(nums) == 1:
            return nums[0]
        while l < r:
            if(r - l == 1):
                return min(nums[r], nums[l])
            elif nums[l] < nums[mid] and nums[r] < nums[l]:
                l = mid
                mid = (r + l)//2
            else:
                r = mid
                mid = (r + l)//2
        return 1