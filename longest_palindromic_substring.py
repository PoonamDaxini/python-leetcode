# problem: https://leetcode.com/problems/longest-palindromic-substring/


class Solution(object):

    def getIndex(self, arr, index, length):
        start = index - length -1
        end = index + length + 1
            
        while(end < len(arr) and arr[start] and arr[end] ):
            if(arr[start] == arr[end]):
                length = length+1
                start = start -1
                end = end+1
            else:
                break;
        
        return length
        
    def longestPalindrome(self, s):
        #manchester algo try
        
        string_length = len(s)
        
        res = '#'.join(s[i:i + 1] for i in range(0, string_length)) 
        res = '#'+res+'#'
        
        string_length = len(res)
        
        resArr = res.split()

        arr = [0]*string_length

        center =0
        # left 
        right = 0
        maxIndex = 0
        
        for i in range(1,string_length):
            mirror = arr[2*center - i]
            
            if(i< right):
                arr[i] = min(mirror, right - i)

            arr[i] = self.getIndex(arr=res, index = i, length = arr[i])
            
            if(i+arr[i] > right):
                center = i
                right = i + arr[i]
                
            if(arr[maxIndex] < arr[i]):
                maxIndex = i
                
        
        start = maxIndex - arr[maxIndex]
        end = maxIndex + arr[maxIndex]
        
        
        return (res[start:end+1]).replace('#','')
    
'''working solution
def getIndex(string, left, right):
    if(right >= len(string)):
        return(0,0)

    start = left
    end = right

    while start >=0 and end < len(string) and string[start] == string[end]:
        start = start -1
        end = end +1

    return (start+1, end-1)
class Solution(object):
   
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 1
        max_string = s[0:1]
        
        string_length = len(s)
        
        start = 0 
        end = 0
        for i in range(string_length):
            left, right = getIndex(s, i, i)
            if right-left > end-start:
                start = left
                end = right
            left, right = getIndex(s, i, i+1)
            if right-left > end-start:
                start = left
                end = right
                
        return s[start:end+1]
       
#         res = '#'.join(s[i:i + 1] for i in range(0, string_length)) 
#         res = '$#'+res+'#@'
        
#         print(res)
        
        #time limit exceeds in this
        if(string_length > 2):
            for l in range(string_length):
                for r in range(l, string_length):
                    new_length = r-l+1
                    sub_str = s[l:r+1]
                    rev_sub_str = sub_str[::-1]
                    if(sub_str == rev_sub_str and max_length < len(sub_str) ):
                            max_length = len(sub_str)
                            max_string = sub_str
        
            return max_string
        elif(string_length == 2 and s[0:1] == s[1:2]):
            return s
        else:
            return max_string
        
        #matrix tried
        matrix = [ [0]*string_length for i in range(string_length)]
        
        for i in range(string_length):
            matrix[i][i] = 1
            
        print(matrix)
        '''
        # for col in range(2, string_length):
        #     for row in range()
