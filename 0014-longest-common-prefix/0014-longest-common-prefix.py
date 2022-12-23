class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        pre = strs[0]
        
        for word in strs:
            
            while not word.startswith(pre):
                # remove the last letter from the prefix-common-word
                pre = pre[:-1]
        
        return pre     