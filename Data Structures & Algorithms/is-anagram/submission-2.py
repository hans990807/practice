class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # list
        # hashmap
        # sort
        return sorted(s) == sorted(t)