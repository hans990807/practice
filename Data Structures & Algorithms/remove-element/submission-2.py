class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer
            # next non val
        insert_point = 0
        for i, num in enumerate(nums):
            if num != val:
                nums[insert_point] = num
                insert_point += 1
        return insert_point
                


