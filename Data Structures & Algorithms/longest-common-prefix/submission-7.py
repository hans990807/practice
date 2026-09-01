class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # anchor the first word, update the output
        # compare alphabet by alphabet, update the output
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i >= len(s) or strs[0][i] != s[i]:
        #             return strs[0][:i]
        # return strs[0]
        # sort, compare the first and last
        if len(strs) == 1:
            return strs[0]
        sorted_strs = sorted(strs)
        i_max = min(len(sorted_strs[0]), len(sorted_strs[1]))
        for i in range(i_max):
            if sorted_strs[0][i] != sorted_strs[-1][i]:
                return sorted_strs[0][:i]
        return sorted_strs[0][:i_max] # 1 also works
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # res = ''
        # for first_word_index, first_word_slice in enumerate(strs[0]):
        #     for each_word in strs:
        #         if first_word_index > len(each_word) - 1 or first_word_slice != each_word[first_word_index]:
        #             return res
        #     res += first_word_slice
        # return res