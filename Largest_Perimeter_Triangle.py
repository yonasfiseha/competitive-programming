#https://leetcode.com/problems/largest-perimeter-triangle/
class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse = True)
        for x, y, z in zip(nums, nums[1:], nums[2:]):
            sums= x + z + y
            if y+z > x:
                return sums
        return 0
    
Solution = Solution()
print(Solution.largestPerimeter(nums=[3,2,3,4]))