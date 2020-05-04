# problem: https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M":1000
        }
        
        
        i=0
        #need to hold previous value for 4,9 etc
        
        length_s = len(s)
        result = 0
        
        while i < length_s:
        
            current = dic[s[i]]
            
            if(i+1 < length_s):
                next_val = dic[s[i+1]]
                
                if(current >= next_val):
                    result = result + current
                    i = i + 1
                else:
                    result = result + next_val - current
                    i = i + 2
            else:
                result = result + current
                i = i + 1 
        return result
                    
