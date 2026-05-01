class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort
        sortedkey_value = collections.defaultdict(list)
        for s in strs:
            sortedkey_value[tuple(sorted(s))].append(s)
        
        return list(sortedkey_value.values())

        # {tuple([0, 1, 2, 1, ..., 4]) : list of strs}
        # count_value = collections.defaultdict(list) #
        # for s in strs:
        #     count = [0] * 26 #?
        #     for chr in s:
        #         count[ord(chr) - ord('a')] += 1
        #     count_value[tuple(count)].append(s)
        
        # res = []
        # for value in count_value.values():
        #     res.append(value)
        # return res


