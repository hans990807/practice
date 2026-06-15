class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore
        res = 0
        count = 0

        for num in nums:
            if count == 0:
                res = num
                count = 1
            elif res == num:
                count += 1
            elif res != num:
                count -= 1
        return res
        
        # 1 sort: O(nlogn), O(n)
        # nums.sort()
        # return nums[len(nums)//2]
        # 2 hashmap, count once great than n/2: O(n), O(n)
        # num_count = collections.defaultdict(int)
        # n = len(nums)
        # for num in nums:
        #     num_count[num] += 1
        #     if num_count[num] > n / 2: #?
        #         return num
        # 3 Boyer Moore O(n), O(1)
        # res, count = 0, 0
        # for num in nums:
        #     if count == 0:
        #         res = num
        #         count = 1
        #     elif num == res:
        #         count += 1
        #     elif num != res: # else
        #         count -= 1
        
        # return res


