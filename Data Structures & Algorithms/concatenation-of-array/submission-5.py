class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        for i, num in enumerate(nums):
            ans[i] = ans[i + len(nums)] = num
        return ans

        # ans = []
        # for i in range(2):
        #     for num in nums:
        #         ans.append(num)
        # return ans


        # wrong, infinite loop
        # for num in nums:
        #     nums.append(num)
        # return nums