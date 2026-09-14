class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap, count and return when > n/2
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > len(nums) / 2:
                return num
        
        # sort, return the mid num
        