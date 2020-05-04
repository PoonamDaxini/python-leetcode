# problem: https://leetcode.com/problems/integer-to-roman/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {
            1:'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: "L",
            90: 'XC',
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }
        
        #0-12 : 13 inputs of dict
        i = 12
        roman_str =''
        div_factor = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        
        while num:
            div = num // div_factor[i] #get quotient
            
            num = num % div_factor[i] # reminder as num
            
            while div:
                roman_str = roman_str + dic[div_factor[i]]
                div = div -1
            i = i-1
            
        return roman_str
