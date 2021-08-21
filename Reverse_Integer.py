class Solution(object):
   
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse_num = 0
        while(x > 0):
            reminder = x % 10 
            reverse_num = (reverse_num *10) + reminder
            x = x//10
        return reverse_num   
            
            
solution = Solution()
solution.reverse(123)