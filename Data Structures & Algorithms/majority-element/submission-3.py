class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1 sort: O(nlogn), O(n)
        # nums.sort()
        # return nums[len(nums)//2]
        # 2 hashmap, count once great than n/2: O(n), O(n)
        num_count = collections.defaultdict(int)
        n = len(nums)
        for num in nums:
            num_count[num] += 1
            if num_count[num] > n / 2: #?
                return num
