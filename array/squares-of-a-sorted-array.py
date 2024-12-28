class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            nums[i] = num**2
        nums.sort()
        return nums