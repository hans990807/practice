class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hasmap: O(n), O(n)
        hashmap = collections.defaultdict(int) # duplicate value? 2 same the most, if happened, the ans would be those two
        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            hashmap[num] = i

        # brute force: O(n^2), O(1)
        # for i in range(len(nums) - 1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        