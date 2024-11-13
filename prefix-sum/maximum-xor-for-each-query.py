class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        '''
        [2,3,4,7]

        [2,1,5,2]
        [5,6,2,5]
        [5,2,6,5]
        |||
         |0
        |0|
        '''
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] ^ nums[i]
        res = []
        for i in range(len(nums)-1,-1,-1):
            res.append(nums[i] ^ ((1 << maximumBit) - 1))
        return res