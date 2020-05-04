# problem: https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        
        length_list = len(strs)
        
        if(length_list == 0):
            return ""
        elif length_list == 1:
            return strs[0]
        
        
#         compare strings, check shortest length string which will be max of prefix

        shortest_length = min(len(ele) for ele in strs)
        is_prefix = True
        
        for i in range(0, shortest_length):
            
            current_prefix = strs[0][i]
            
            for str_list in strs:
                if str_list[i] != current_prefix:
                    is_prefix = False
            
            
            if(not is_prefix):
                break
            else:
                prefix = prefix + current_prefix
                
        return prefix
