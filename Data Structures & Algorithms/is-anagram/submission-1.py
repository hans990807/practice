from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # compare if two hashmaps are the same
        if len(s) != len(t):
            return False
        
        hashmap_s = collections.defaultdict(int)
        hashmap_t = collections.defaultdict(int)

        for i in range(len(s)):
            hashmap_s[s[i]] += 1
            hashmap_t[t[i]] += 1
        
        return hashmap_s == hashmap_t


        # sort
        # O(nlogn), O(n)

        # s_sorted = sorted(s)
        # t_sorted = sorted(t)

        # return s_sorted == t_sorted
        