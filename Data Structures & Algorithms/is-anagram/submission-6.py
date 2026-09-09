class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # list
        # if len(s) != len(t):
        #     return False
        # # count_s = count_t = [0] * 26 會綁定！
        # # mutable: list, dict, set 都會綁定, immutable int, float, bool, tuple都不會
        # count_s = [0] * 26
        # count_t = [0] * 26
        # for i in range(len(s)):
        #     count_s[ord(s[i]) - ord('a')] += 1
        #     count_t[ord(t[i]) - ord('a')] += 1
        # return count_s == count_t

        # hashmap
        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            if s[i] in hashmap_s:
                hashmap_s[s[i]] += 1
            else:
                hashmap_s[s[i]] = 1
            if t[i] in hashmap_t:
                hashmap_t[t[i]] += 1
            else:
                hashmap_t[t[i]] = 1
        
        return hashmap_s == hashmap_t


        
        # # sort
        # return sorted(s) == sorted(t)