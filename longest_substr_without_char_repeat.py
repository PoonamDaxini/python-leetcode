#problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(not s or not len(s) ):
            return 0
        
        max_length = start = 0
        char = dict()
        
        for i in range(len(s)):
            if(s[i] in char and start <= char[s[i]]):
                start = char[s[i]] + 1
            else:
                max_length = max(max_length, i- start+1)
                
            char[s[i]] = i
            
        return max_length
