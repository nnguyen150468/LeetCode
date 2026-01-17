class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1  2  3  4]
        [1  1  1  1]
        
        [1  1  2  6]
            12   8   6  

        suffix = 1
                24

        
        [      8   6 ]
        '''
        prefix = [1] * len(nums)
        suffix = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix *= nums[i+1]
            prefix[i] *= suffix

        return prefix