class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) - 1
        i = 0   
    
        def swap(i, j):
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1

        return nums

        '''
        [0, 1, 2]
            l
            r
               i
        '''