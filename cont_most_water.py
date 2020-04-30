# problem : https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i=0
        j=len(height) -1
        
        while(i<j):
            min_area = min(height[i], height[j])
            max_area = max(max_area, min_area * (j-i))
            
            if(height[i] < height[j]):
                i = i+1
            else:
                j = j-1
        
        return max_area
                
# O(n) space and time complexity
