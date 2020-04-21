#problem : https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = False
        
        if (x < 0):
		    x = x * -1
		    flag = True
            
        rev = 0
        while(x!=0):
            rev = rev*10 + x%10
            x = x/10
        
        if(flag):
            if(rev > (2 ** 31)):
                return 0
            rev = rev * -1
        
        
        elif(rev > (2 ** 31 - 1)):
            return 0
        
        return rev
