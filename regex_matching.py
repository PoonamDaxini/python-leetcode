# problem https://leetcode.com/problems/regular-expression-matching

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        length_s = len(s)
        length_p = len(p)
        
        arr = [[False for x in range(length_p + 1)] for y in range(length_s + 1)] 
        
        arr[0][0] = True
        for j in range(1, length_p+1):
            if p[j-1] == '*':
                arr[0][j] = arr[0][j-2]        
       
        
        for i in range(1, length_s + 1):
            for j in range(1, length_p +1):
                if(s[i-1] == p[j-1] or p[j-1] =='.'):
                    arr[i][j] = arr[i-1][j-1]
                elif(p[j-1]=="*"):
                    if(arr[i][j-2]):
                        arr[i][j] = arr[i][j-2]
                    elif(s[i-1] == p[j-2] or p[j-2] == '.'):
                        arr[i][j] = arr[i][j] or arr[i-1][j]
                else:
                    arr[i][j] = False
                        
        return arr[length_s][length_p]

#time and space complexity: O(length_s * length_p)
