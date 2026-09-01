class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap two pass
        hashmap = {}
        for i, num in enumerate(nums):
            hashmap[num] = i
        
        for j, num in enumerate(nums):
            diff = target - num
            if diff in hashmap and hashmap[diff] != j:
                return [j, hashmap[diff]]

        # sort
        # nums_copy = []
        # for i, num in enumerate(nums):
        #     nums_copy.append([num, i])
        
        # nums_copy.sort()
        # l, r = 0, len(nums_copy) - 1
        # while l < r:
        #     if nums_copy[l][0] + nums_copy[r][0] > target:
        #         r -= 1
        #     elif nums_copy[l][0] + nums_copy[r][0] < target:
        #         l += 1
        #     else:
        #         min_i = min(nums_copy[l][1], nums_copy[r][1])
        #         max_i = max(nums_copy[l][1], nums_copy[r][1])
        #         return [min_i, max_i]

        


        # hashmap one pass O(n), O(n)
        # hashmap = collections.defaultdict(int)
        # for i, num in enumerate(nums):
        #     if target - num in hashmap:
        #         return [hashmap[target - num], i]
        #     hashmap[num] = i
        
        # brute force O(n^2), O(1)
        # for left_index, left_num in enumerate(nums):
        #     for right_index in range(left_index + 1, len(nums)):
        #         if left_num + nums[right_index] == target:
        #             return [left_index, right_index]


        