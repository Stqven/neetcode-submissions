class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2 # 0
            if(nums[mid] == target):
                return mid
            if(nums[mid] >= nums[l]):
                if(nums[l] <= target < nums[mid]):
                    #we go left
                    r = mid - 1
                else:
                    #we go right
                    l = mid + 1
            else:
                if(nums[r] >= target > nums[mid]):
                    l = mid + 1
                else:
                    r = mid -1

        return -1



        

            

