#problem : https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        input1 = nums2 if len(nums1) > len(nums2) else nums1
        
        input2 = nums1 if len(nums1) > len(nums2) else nums2
        
        len_input1 = len(input1)
        len_input2 = len(input2)
        
        start = 0
        end = len_input1
        
        while(start <= end):
            partitionx = (start + end) /2;
            
            partitiony = (len_input1 + len_input2 +1)/2 - partitionx
            
            # print(partitionx, partitiony)
            leftx = float("-inf") if partitionx == 0 else input1[partitionx-1]
            rightx = float("inf") if partitionx == len_input1 else  input1[partitionx]
            
            lefty = float("-inf") if partitiony == 0 else input2[partitiony-1]
            righty = float("inf") if partitiony == len_input2 else  input2[partitiony]
            
            # print(leftx, lefty, rightx, righty)
            if(lefty <= rightx and leftx <= righty):
                # found
                # print("found")
                if((len_input1+len_input2) %2 == 0):
                    # even -> avg find
                    return (float)(max(leftx, lefty) + min(rightx, righty))/2
                else:
#                     odd max of left is answer
                    return max(leftx, lefty)
            elif(lefty > rightx):
        
                # print("change end")
                start = partitionx + 1
            
            else:
                
                # print("change start")
                end = partitionx - 1
            
