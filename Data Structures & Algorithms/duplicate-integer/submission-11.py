class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # brute force
        # hashmap
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

        # sort
