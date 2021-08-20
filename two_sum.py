# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
      
       
        ln= len(nums)
        for i in range(ln):
            for j in range(i+1 , ln):
                if nums[i] + nums[j] == target:
                 return [i, j]
     
