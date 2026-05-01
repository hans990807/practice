class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i, current_chr in enumerate(strs[0]):
            for current_word in strs:
                if len(current_word) - 1 < i or current_word[i] != current_chr:
                    return res
            res += current_chr
        return res



























        
        # res = ''
        # for first_word_index, first_word_slice in enumerate(strs[0]):
        #     for each_word in strs:
        #         if first_word_index > len(each_word) - 1 or first_word_slice != each_word[first_word_index]:
        #             return res
        #     res += first_word_slice
        # return res