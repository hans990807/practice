class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left_index, left_num in enumerate(nums):
            for right_index in range(left_index + 1, len(nums)):
                if left_num + nums[right_index] == target:
                    return [left_index, right_index]


        