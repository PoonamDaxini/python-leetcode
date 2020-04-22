#Problem : https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if(x < 0):
            return False
        
      
        
        length = len(x)
        
        mid = length / 2
        
        for i in range(0, mid):
            if(x[i] != x[length -1 - i]):
                return False
        return True
