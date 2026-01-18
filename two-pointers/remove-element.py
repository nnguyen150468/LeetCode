class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            while l < r and nums[r] == val:
                r -= 1
            while l < r and nums[l] != val:
                l += 1
            num = nums[r]
            nums[r] = nums[l]
            nums[l] = num
            l += 1
            r -= 1
        return l + 1

        '''
        [0,1,4,0,3,2,2,2]
                 l r 
        '''
            