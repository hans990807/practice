class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tuple_str = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tuple_str[tuple(count)].append(s)
        
        res = []
        for key, value in tuple_str.items():
            res.append(value)
        return res