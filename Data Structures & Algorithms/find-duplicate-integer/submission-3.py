class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #n = ceiling of numbers ?
        # whole array is 1- len(nums) - 1
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        
        return slow
            

