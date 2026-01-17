class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        [1  2  3  4]
        [1  1  1  1]
        [24 12 4 1]
        [1, 1, 2, 6]

        
        [      8   6 ]
        '''
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])
        return res