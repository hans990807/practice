class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums) - 1
        while i <= n:
            if nums[i] == val:
                nums[i] = nums[n]
                n -= 1
            else:
                i += 1
        return n + 1
        
        
        
        # # two pointer
        #     # next non val
        # insert_point = 0
        # for i, num in enumerate(nums):
        #     if num != val:
        #         nums[insert_point] = num
        #         insert_point += 1
        # return insert_point
            