class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort
        anagrams = collections.defaultdict(list) # sorted string : anagrams
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        
        res = []
        for value in anagrams.values():
            res.append(value)
        return res
        # # counter (list or hhmap (asx))
        # tuple_str = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     tuple_str[tuple(count)].append(s)
        
        # res = []
        # for value in tuple_str.values():
        #     res.append(value)
        # return res