class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # voting
        count = 0
        res = 0

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        return res

            

        # # hashmap, count and return when > n/2
        # count = collections.defaultdict(int)
        # for num in nums:
        #     count[num] += 1
        #     if count[num] > len(nums) // 2:
        #         return num
        
        # # sort, return the mid num
        # sorted_nums = sorted(nums)
        # return sorted_nums[len(nums) // 2]