#problem: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        no_of_elements = len(nums)
        complements = dict()
        
        for i in range(no_of_elements):
            comp = target - nums[i]

            if nums[i] in complements:
                return [complements[nums[i]], i]
            else:
                complements[comp] = i
                
        '''
        for i in range(no_of_elements):
            for j in range(i+1, no_of_elements):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]
        '''
