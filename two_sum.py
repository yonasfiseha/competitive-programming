# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    
    
    ln= len(nums)
    for i in range(ln):
        for j in range(i+1 , ln):
            if nums[i] + nums[j] == target:
                return [i, j]
    
print(twoSum([2,7,11,15], 9))
