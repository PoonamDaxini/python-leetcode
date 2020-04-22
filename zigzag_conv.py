#problem : https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        string_length = len(s)
        
        if(numRows == 1 or numRows >= string_length):
            return s
        
        res = [''] * numRows
        row = 0
        
        for i in range(string_length):
            res[row] += s[i]

            if(row == 0):
                step = 1
            if(row == numRows -1):
                step = -1       
                
            row = row + step
        
      
        
        return "".join(res)
    
       
