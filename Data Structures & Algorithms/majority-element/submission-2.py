class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1 sort: O(nlogn), O(n)
        nums.sort()
        return nums[len(nums)//2]
        # 2 hashmap, count once great than n/2: O(n), O(n)