#problem: https://leetcode.com/problems/string-to-integer-atoi/
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        str = str.strip()
        
        start=0
        negative = False
        
        
        if(len(str) <= 0):
            return 0
        
        if(str[0] == '-'):
            negative = True
            start=1
        
        elif(str[0] == '+'):
            negative = False
            start=1
            
        elif(not str[0].isdigit()): 
            return 0
        
        digit =0
        
        
        for i in range(start, len(str)):
            if(str[i].isdigit()):
                digit = digit * 10 + int(str[i])
            else:
                break
        
        if(negative):
            max_no = (2 ** 31)
            if(digit > max_no):
                return max_no * -1
            digit = digit * -1
        
        
        elif(digit > (2 ** 31 - 1)):
            return (2 ** 31 - 1)
        
        return digit
