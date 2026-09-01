class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort lexicographically
        sorted_strs = sorted(strs)
        
        first = sorted_strs[0]
        last = sorted_strs[-1]
        
        # Compare character by character
        for i in range(len(first)):
            if first[i] != last[i]:
                return first[:i]
                
        # If the loop finishes, 'first' is entirely the common prefix
        return first