class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare if two hashmaps are the same
        # sort

        s_sorted = sorted(s)
        t_sorted = sorted(t)

        return s_sorted == t_sorted
        