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
        xor_table = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            print(i, len(nums))
            xor_table[i] = xor_table[i-1] ^ nums[i]
        res = []
        for i in range(len(nums)-1,-1,-1):
            res.append(xor_table[i] ^ (2**maximumBit - 1))
        return res