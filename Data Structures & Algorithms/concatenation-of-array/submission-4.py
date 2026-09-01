class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        # wrong, infinite loop
        # for num in nums:
        #     nums.append(num)
        # return nums