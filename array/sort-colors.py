class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        curr = 0
        i = 0
        while curr < 3 and i < len(nums):
            if seen[curr] > 0:
                nums[i] = curr
                seen[curr] -= 1
                i += 1
            else:
                curr += 1
        return nums