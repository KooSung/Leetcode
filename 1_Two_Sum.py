class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            number = target - nums[i]
            if number in nums[i+1:]:
                return [i, nums[i+1:].index(number)+i+1]
