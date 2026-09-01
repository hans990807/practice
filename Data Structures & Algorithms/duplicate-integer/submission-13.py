class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # hashmap
        # seen = set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         return True
        # return False

        # sort
        sorted_num = sorted(nums)
        for i in range(len(sorted_num) - 1): #?
            if sorted_num[i] == sorted_num[i + 1]:
                return True
        return False

